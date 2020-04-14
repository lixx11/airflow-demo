#!/usr/bin/env python

import glob
import sys
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR, 'data_source'))
sys.path.append(os.path.join(ROOT_DIR, 'signal'))

from zs_signal import Signal
from zs_signal.ttypes import SignalReply
from data_source import DataSource
from data_source.ttypes import DataRequest
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class SignalHandler:
    def __init__(self):
        pass

    def CalcSignal(self, request):
        transport = TSocket.TSocket('localhost', 10000)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = DataSource.Client(protocol)
        transport.open()
        data_request = DataRequest()
        data_request.name = 'demo'
        data_reply = client.fetch_data(data_request)
        transport.close()

        sig = data_reply.a + data_reply.b
        reply = SignalReply()
        reply.sig = sig
        return reply


if __name__ == '__main__':
    handler = SignalHandler()
    processor = Signal.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=10001)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
