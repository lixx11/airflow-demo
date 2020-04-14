#!/usr/bin/env python

import os
import sys
import glob
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR, 'data_source'))

from data_source import DataSource
from data_source.ttypes import DataRequest
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    transport = TSocket.TSocket('localhost', 10000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = DataSource.Client(protocol)
    transport.open()

    request = DataRequest()
    request.name = 'test'
    reply = client.fetch_data(request)
    print(reply.a, reply.b)
    transport.close()


if __name__ == '__main__':
    main()
