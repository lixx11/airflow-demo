#!/usr/bin/env python
import time
import sys

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dataflow_demo.servers.auth_server.auth_rpc import Auth


class AuthAPI:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.transport = TSocket.TSocket(host, port)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.transport.open()
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = self._create_client()

    def _create_client(self):
        client = Auth.Client(self.protocol)
        return client
    
    def close(self):
        self.transport.close()
    
    def authenticate(self, username, password):
        token = self.client.authenticate(username, password)
        if token == 'Not Found':
            print(f'ERROR! Authentication failed for {username} with '
                   '{password}!')
            return None
        else:
            return token

    def has_perm(self, token, api):
        return self.client.has_perm(token, api)


if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]
    username = 'zhuoshi'
    password = 'zhuoshi'
    print('Connecting to %s:%s' % (host, port))

    api = AuthAPI(host, int(port))
    token = api.authenticate(username, password)
    print(f'Token of {username}-{password}: {token}')

    check_api = 'any api'
    has_perm = api.has_perm(token, check_api)
    print(f'Permission granted for {check_api}!')
    api.close()
