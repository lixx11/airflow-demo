#!/usr/bin/env python

import os
import sys
import glob
import time
import pandas as pd
import pyarrow as pa

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dataflow_demo.services.signal_service.signal_rpc import Signal
from dataflow_demo import utils


def main():
    transport = TSocket.TSocket('localhost', 10001)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Signal.Client(protocol)
    transport.open()

    context = pa.default_serialization_context()
    response = client.calc_signal('20200418', commit=True)
    df = context.deserialize(response)
    print(df.head())
    transport.close()


if __name__ == '__main__':
    main()
