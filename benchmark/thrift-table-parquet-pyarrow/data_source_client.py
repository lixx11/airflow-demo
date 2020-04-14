#!/usr/bin/env python

import os
import sys
import glob
import io
import time
import pandas as pd
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR, 'data_source'))

from data_source import DataSource
from data_source.ttypes import Table
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    nb_tests = int(sys.argv[1])
    transport = TSocket.TSocket('localhost', 10000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = DataSource.Client(protocol)
    transport.open()

    t1 = time.time()
    for _ in range(nb_tests):
        reply = client.fetch_data(name='demo')
        f = io.BytesIO(reply.data)
        data = pd.read_parquet(f, engine='pyarrow')
    t2 = time.time()
    print('%.3E' % ((t2-t1)/nb_tests))
    transport.close()


if __name__ == '__main__':
    main()
