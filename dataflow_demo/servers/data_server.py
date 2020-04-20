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


class DataServer:
    def __init__(self, conf_file):
        with open(conf_file, 'r') as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
        self.host = conf['data_server']['rpc']['host']
        self.port = conf['data_server']['rpc']['port']
        my_db, mg_db = utils.init_db(conf['data_server'])
        self.handler = self.Handler(my_db, mg_db)
        self.processor = DataSource.Processor(self.handler)
        self.transport = TSocket.TServerSocket(
            host=self.host, port=self.port)
        self.tfactory = TTransport.TBufferedTransportFactory()
        self.pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        self.server = TServer.TThreadedServer(
            self.processor, self.transport, self.tfactory, self.pfactory)
    
    def serve(self):
        self.server.serve()
        
    
    class Handler:
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
        
        def write_stock_tick(self, table):
            date = table.date
            df = self.context.deserialize(table.data)
            df.to_sql(date, self.my_db['stock_tick'], if_exists='replace', index=False)
        
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

        def write_stock_daily(self, table):
            self.mg_db['market_daily']['stock'].insert_one({
                'date': table.date,
                'data': table.data,
                'timestamp': table.timestamp,
                'user': table.user,
                'comment': table.comment,
            })
        
        def write_signal(self, table):
            self.mg_db['model']['signal'].insert_one({
                'date': table.date,
                'data': table.data,
                'timestamp': table.timestamp,
                'user': table.user,
                'comment': table.comment,
                'sig_type': table.sig_type,
            })

        def read_signal(self, date, sig_type):
            records = self.mg_db['model']['signal'].find(
                {'date': date, 'sig_type': sig_type}
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
                table.sig_type = record['sig_type']
                return table


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You must provide a conf file!!!')
        sys.exit()
    else:
        conf_file = sys.argv[1]
        print('Reading conf from %s' % conf_file)

    data_server = DataServer(conf_file)

    print('Starting the server...')
    data_server.serve()
    print('done.')
