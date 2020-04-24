#!/usr/bin/env python

import sys
import yaml

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from dataflow_demo.servers.auth_server.auth_rpc import Auth


class AuthServer:
    def __init__(self, conf_file):
        with open(conf_file, 'r') as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
        auth_conf = conf['auth_server']
        self.host = auth_conf['rpc']['host']
        self.port = auth_conf['rpc']['port']
        self.handler = self.Handler(auth_conf['auth_file'])
        self.processor = Auth.Processor(self.handler)
        self.transport = TSocket.TServerSocket(
            host=self.host, port=self.port)
        self.tfactory = TTransport.TBufferedTransportFactory()
        self.pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        self.server = TServer.TThreadedServer(
            self.processor, self.transport, self.tfactory, self.pfactory)
    
    def serve(self):
        self.server.serve()
    
    def close(self):
        self.transport.close()
    
    class Handler:
        def __init__(self, auth_file):
            with open(auth_file, 'r') as f:
                auth_conf = yaml.load(f, Loader=yaml.FullLoader)
            auth_dict = {}  # (username, password) -> token
            perm_dict = {}  # token -> permissions
            for user in auth_conf.values():
                auth_dict[
                    (user['username'], user['password'])
                ] = user['token']
                perm_dict[user['token']] = user['permissions']
            self.auth_dict = auth_dict
            self.perm_dict = perm_dict
        
        def authenticate(self, username, password):
            token = self.auth_dict.get((username, password), 'Not Found')
            return token

        def has_perm(self, token, api):
            if token not in self.perm_dict:
                return False
            permissions = self.perm_dict[token]
            if permissions == '__all__':
                return True
            elif api in permissions:
                return True
            return False
        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You must provide a conf file!!!')
        sys.exit()
    else:
        conf_file = sys.argv[1]
        print('Reading configuration from %s' % conf_file)

    auth_server = AuthServer(conf_file)

    print('Starting the auth server...')
    auth_server.serve()
    print('done.')
