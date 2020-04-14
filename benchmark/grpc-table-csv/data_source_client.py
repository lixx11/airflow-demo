import grpc
import io
import sys
import time
import pandas as pd
import data_source_pb2
import data_source_pb2_grpc


def run():
    nb_tests = int(sys.argv[1])
    with grpc.insecure_channel(
        'localhost:10000',
        options=[
            ('grpc.max_send_message_length', 1*1024*1024*1024),
            ('grpc.max_receive_message_length', 1*1024*1024*1024),
        ]) as channel:
        stub = data_source_pb2_grpc.DataSourceStub(channel)
        t1 = time.time()
        for _ in range(nb_tests):
            response = stub.FetchData(data_source_pb2.Request(name='demo'))
            f = io.StringIO(response.data)
            f.seek(0)
            data = pd.read_csv(f)
        t2 = time.time()
        print('%.3E' % ((t2-t1)/nb_tests))


if __name__ == '__main__':
    run()
