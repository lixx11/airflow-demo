#!/usr/bin/env python
import time
import sys

from dataflow_demo.services.signal_service.signal_rpc import Signal
from dataflow_demo.clients.base_api import BaseAPI
from dataflow_demo import utils
from dataflow_demo.utils import NotLoginError, check_login


class SignalAPI(BaseAPI):
    def _create_client(self):
        client = Signal.Client(self.protocol)
        return client

    @check_login
    def calc_signal(self, date, commit=False, comment=''):
        self.client.calc_signal(date, commit=commit, comment=comment)
    

if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]
    print('Connecting to %s:%s' % (host, port))

    signal_df = utils.build_dummy_signal_table()

    api = SignalAPI(host, port)
    api.authenticate('zhuoshi', 'zhuoshi')

    api.calc_signal('20200418', commit=True, comment='api test')
    print('Passed all tests.')

    api.close()
