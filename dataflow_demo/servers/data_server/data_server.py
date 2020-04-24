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

from dataflow_demo.servers.data_server.data_source_rpc import DataSource
from dataflow_demo.servers.data_server.data_source_rpc.ttypes import (
    VersionedTable, 
    UnversionedTable,
)
from dataflow_demo.clients.auth_api import AuthAPI
from dataflow_demo.servers.data_server import utils
from dataflow_demo.utils import check_perm


class DataServer:
    def __init__(self, conf_file):
        with open(conf_file, 'r') as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
        self.host = conf['data_server']['rpc']['host']
        self.port = conf['data_server']['rpc']['port']
        my_db, mg_db = utils.init_db(conf['data_server'])

        self.auth_host = conf['auth_server']['rpc']['host']
        self.auth_port = conf['auth_server']['rpc']['port']
        self.auth_api = AuthAPI(self.auth_host, self.auth_port)

        self.handler = self.Handler(my_db, mg_db, self.auth_api)
        self.processor = DataSource.Processor(self.handler)
        self.transport = TSocket.TServerSocket(
            host=self.host, port=self.port)
        self.tfactory = TTransport.TBufferedTransportFactory()
        self.pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        self.server = TServer.TThreadedServer(
            self.processor, self.transport, self.tfactory, self.pfactory)
        
    def serve(self):
        self.server.serve()
    
    def close(self):
        self.auth_api.close()
        self.transport.close()
        
    
    class Handler:
        def __init__(self, my_db, mg_db, auth_api):
            self.my_db = my_db
            self.mg_db = mg_db
            self.auth_api = auth_api
            self.context = pa.default_serialization_context()

        @check_perm
        def read_stock_tick(self, token, date):
            df = pd.read_sql_table(date, self.my_db['stock_tick'])
            table = UnversionedTable()
            table.date = date
            table.data = self.context.serialize(df).to_buffer().to_pybytes()
            return table
        
        @check_perm
        def write_stock_tick(self, token, table):
            date = table.date
            df = self.context.deserialize(table.data)
            df.to_sql(date, self.my_db['stock_tick'], if_exists='replace', index=False)
            return True
        
        @check_perm
        def read_stock_daily(self, token, date):
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

        @check_perm
        def write_stock_daily(self, token, table):
            self.mg_db['market_daily']['stock'].insert_one({
                'date': table.date,
                'data': table.data,
                'timestamp': table.timestamp,
                'user': table.user,
                'comment': table.comment,
            })
            return True
        
        @check_perm
        def write_signal(self, token, table):
            self.mg_db['model']['signal'].insert_one({
                'date': table.date,
                'data': table.data,
                'timestamp': table.timestamp,
                'user': table.user,
                'comment': table.comment,
                'sig_type': table.sig_type,
            })
            return True

        @check_perm
        def read_signal(self, token, date, sig_type):
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
