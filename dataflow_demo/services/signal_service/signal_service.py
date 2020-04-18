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

from dataflow_demo.services.signal_service.signal_rpc import Signal
from dataflow_demo.services.base_service import BaseService


class SignalService(BaseService):
    def __init__(self, conf_file):
        super(SignalService, self).__init__(conf_file)
        with open(conf_file, 'r') as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
        service_conf = conf['signal_service']
        user = service_conf['data_server_auth']['user']
        password = service_conf['data_server_auth']['password']
        self.login_data_server(user, password)

        self.host = service_conf['rpc']['host']
        self.port = service_conf['rpc']['port']
        self.handler = self.Handler(self.data_api)
        self.processor = Signal.Processor(self.handler)
        self.transport = TSocket.TServerSocket(
            host=self.host, port=self.port)
        self.tfactory = TTransport.TBufferedTransportFactory()
        self.pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        self.server = TServer.TSimpleServer(
            self.processor, self.transport, self.tfactory, self.pfactory)
    
    def serve(self):
        self.server.serve()
    
    class Handler:
        def __init__(self, data_api):
            self.data_api = data_api
            self.context = pa.default_serialization_context()

        def calc_signal(self, date, commit=False, comment=''):
            df = self.data_api.read_stock_daily(date)
            df['signal'] = 666
            data = self.context.serialize(df).to_buffer().to_pybytes()
            if commit:
                self.data_api.write_signal(
                    date, df, 'demo_sig', comment=comment)
            return data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('You must provide a conf file!!!')
        sys.exit()
    else:
        conf_file = sys.argv[1]
        print('Reading conf from %s' % conf_file)

    signal_service = SignalService(conf_file)

    print('Starting the service...')
    signal_service.serve()
    print('done.')