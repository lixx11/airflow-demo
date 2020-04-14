import grpc

import simple_pb2
import simple_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = simple_pb2_grpc.SignalStub(channel)
        response = stub.Sum(simple_pb2.signalRequest(a=1, b=2))
    print("Sum: %f" % response.sum)


if __name__ == '__main__':
    run()
