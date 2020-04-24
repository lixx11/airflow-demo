import pyarrow as pa

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dataflow_demo.clients.auth_api import AuthAPI
from dataflow_demo.utils import NotLoginError


class BaseAPI:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.transport = TSocket.TSocket(host, port)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.transport.open()
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = self._create_client()
        self._context = pa.default_serialization_context()
        self.__login = False
    
    def _create_client(self):
        raise NotImplementedError

    def authenticate(self, username, password, host, port):
        auth_api = AuthAPI(host, port)
        self.token = auth_api.authenticate(username, password)
        if self.token is not None:
            self.__login = True
            self.username = username
            self.password = password
        else:
            self.__login = False
        auth_api.close()
    
    def is_login(self):
        return self.__login

    def close(self):
        self.transport.close()
