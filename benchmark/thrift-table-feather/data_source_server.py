#!/usr/bin/env python

import os
import glob
import sys
import io
import pandas as pd
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR, 'data_source'))

from data_source import DataSource
from data_source.ttypes import Table
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


N = 1000000
DATA = pd.DataFrame({
    'col1': [1] * N,
    'col2': [1.] * N,
    'col3': ['abc'] * N
})


class DataSourceHandler:
    def __init__(self):
        pass

    def fetch_data(self, request):
        table = Table()
        f = io.BytesIO()
        DATA.to_feather(f)
        table.data = f.getvalue()
        return table


if __name__ == '__main__':
    handler = DataSourceHandler()
    processor = DataSource.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=10000)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
