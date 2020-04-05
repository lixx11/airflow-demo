import grpc
import os
import sys

from concurrent import futures

import signal_pb2
import signal_pb2_grpc

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from data_source import data_source_pb2
from data_source import data_source_pb2_grpc


class Signal(signal_pb2_grpc.SignalServicer):

    def CalcSignal(self, request, context):
        with grpc.insecure_channel('localhost:10000') as channel:
            stub = data_source_pb2_grpc.DataSourceStub(channel)
            response = stub.FetchData(data_source_pb2.DataRequest(name='dummy'))
        sig = response.a + response.b
        return signal_pb2.SignalReply(sig=sig)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    signal_pb2_grpc.add_SignalServicer_to_server(Signal(), server)
    server.add_insecure_port('[::]:10001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
