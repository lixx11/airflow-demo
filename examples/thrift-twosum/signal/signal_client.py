#!/usr/bin/env python

import sys
import os
import glob
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ROOT_DIR, 'gen-py'))

from zs_signal import Signal
from zs_signal.ttypes import SignalRequest
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    transport = TSocket.TSocket('localhost', 10001)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Signal.Client(protocol)
    transport.open()

    request = SignalRequest()
    request.name = 'test'
    reply = client.CalcSignal(request)
    print(reply.sig)
    transport.close()


if __name__ == '__main__':
    main()
