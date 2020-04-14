import grpc
from concurrent import futures

import simple_pb2
import simple_pb2_grpc


class Signal(simple_pb2_grpc.SignalServicer):

    def Sum(self, request, context):
        res = request.a + request.b
        return simple_pb2.signalReply(sum=res)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_pb2_grpc.add_SignalServicer_to_server(Signal(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
