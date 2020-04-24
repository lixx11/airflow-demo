#!/usr/bin/env python

import sys
import time

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dataflow_demo.servers.auth_server.auth_rpc import Auth


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    api = sys.argv[3]
    print('Checking api(%s) permission for %s-%s' % (api, username, password))
    transport = TSocket.TSocket('localhost', 9999)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Auth.Client(protocol)
    transport.open()

    token = client.authenticate(username, password)
    print('Token for %s-%s: %s' % (username, password, token))
    response = client.has_perm(token=token, api=api)
    if response:
        print('Permission granted!')
    else:
        print('Permission denied!')

    transport.close()


if __name__ == '__main__':
    main()
