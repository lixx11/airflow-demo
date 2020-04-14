#!/usr/bin/env python

import os
import glob
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR, 'data_source'))

from data_source import DataSource
from data_source.ttypes import DataReply
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class DataSourceHandler:
    def __init__(self):
        pass

    def fetch_data(self, request):
        reply = DataReply()
        reply.a = 1
        reply.b = 2
        return reply


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
