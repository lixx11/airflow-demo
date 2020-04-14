import grpc

import signal_pb2
import signal_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:10001') as channel:
        stub = signal_pb2_grpc.SignalStub(channel)
        response = stub.CalcSignal(signal_pb2.SignalRequest(name='dummy'))
    print("Signal: %.2f" % response.sig)


if __name__ == '__main__':
    run()
