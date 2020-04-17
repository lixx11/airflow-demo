#!/usr/bin/env python

import glob
import os
import sys
import yaml
import pandas as pd
import pyarrow as pa

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from dataflow_demo.servers.data_source_rpc import DataSource
from dataflow_demo.servers.data_source_rpc.ttypes import (
    VersionedTable, 
    UnversionedTable,
)
from dataflow_demo.servers import utils


N = 10000
DATA = pd.DataFrame({
    'col1': [1] * N,
    'col2': [1.] * N,
    'col3': ['abc'] * N
})


class DataSourceHandler:
    def __init__(self, my_db, mg_db):
        self.my_db = my_db
        self.mg_db = mg_db
        self.context = pa.default_serialization_context()

    def read_stock_tick(self, date):
        df = pd.read_sql_table(date, self.my_db['stock_tick'])
        table = UnversionedTable()
        table.date = date
        table.data = self.context.serialize(df).to_buffer().to_pybytes()
        return table
    
    def write_stock_tick(self, request):
        date = request.date
        df = self.context.deserialize(request.data)
        df.to_sql(date, self.my_db['stock_tick'], if_exists='replace')
    
    def read_stock_daily(self, date):
        records = self.mg_db['market_daily']['stock'].find(
            {'date': date}
        ).sort('timestamp', -1)
        if records.count == 0:
            print('ERROR! NO DATA FOUND!')
        else:
            record = records.next()
            table = VersionedTable()
            table.date = date
            table.data = record['data']
            table.timestamp = record['timestamp']
            table.user = record['user']
            table.comment = record['comment']
            return table

    def write_stock_daily(self, request):
        self.mg_db['market_daily']['stock'].insert_one({
            'date': request.date,
            'data': request.data,
            'timestamp': request.timestamp,
            'user': request.user,
            'comment': request.comment,
        })


if __name__ == '__main__':
    # parse conf file
    if len(sys.argv) < 2:
        print('You must provide a conf file!!!')
        sys.exit()
    else:
        conf_file = sys.argv[1]
        print('Reading conf from %s' % conf_file)
    with open(conf_file, 'r') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    # initilize databases
    my_db, mg_db = utils.init_db(conf['data_server'])

    # setup rpc server
    rpc_conf = conf['rpc']
    handler = DataSourceHandler(my_db, mg_db)
    processor = DataSource.Processor(handler)
    transport = TSocket.TServerSocket(
        host=rpc_conf['host'], port=rpc_conf['port'])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
