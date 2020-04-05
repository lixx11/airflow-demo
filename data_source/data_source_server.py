import os
import sys
import grpc

from concurrent import futures

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from data_source import data_source_pb2
from data_source import data_source_pb2_grpc


class DataSource(data_source_pb2_grpc.DataSourceServicer):

    def FetchData(self, request, context):

        return data_source_pb2.DataReply(a=1, b=2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_source_pb2_grpc.add_DataSourceServicer_to_server(DataSource(), server)
    server.add_insecure_port('[::]:10000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
