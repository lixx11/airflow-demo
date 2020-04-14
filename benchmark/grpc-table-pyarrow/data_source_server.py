import os
import sys
import grpc
import io
import pandas as pd
import pyarrow as pa
from concurrent import futures

import data_source_pb2
import data_source_pb2_grpc


N = 1000000
DATA = pd.DataFrame({
    'col1': [1] * N,
    'col2': [1.] * N,
    'col3': ['abc'] * N
})


class DataSource(data_source_pb2_grpc.DataSourceServicer):

    def FetchData(self, request, context):
        response = data_source_pb2.Response()
        context = pa.default_serialization_context()
        response.data = context.serialize(DATA).to_buffer().to_pybytes()
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_source_pb2_grpc.add_DataSourceServicer_to_server(DataSource(), server)
    server.add_insecure_port('[::]:10000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
