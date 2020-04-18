#!/usr/bin/env python

import pyarrow as pa
import yaml

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dataflow_demo.clients.data_api import DataAPI
from dataflow_demo.utils import NotLoginError, check_login


class BaseService:
    def __init__(self, conf_file):
        with open(conf_file, 'r') as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
        host = conf['data_server']['rpc']['host']
        port = conf['data_server']['rpc']['port']
        self.data_api = DataAPI(host, port)

    def login_data_server(self, username, password):
        self.data_api.authenticate(username, password)
