import grpc

import data_source_pb2
import data_source_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:10000') as channel:
        stub = data_source_pb2_grpc.DataSourceStub(channel)
        response = stub.FetchData(data_source_pb2.DataRequest(name='dummy'))
    print("Data fetched: %.2f %.2f" % (response.a, response.b))


if __name__ == '__main__':
    run()
