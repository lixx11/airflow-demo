#!/usr/bin/env python
import time
import sys

from dataflow_demo.servers.data_source_rpc import DataSource
from dataflow_demo.servers.data_source_rpc.ttypes import (
    VersionedTable,
    UnversionedTable,
)

from dataflow_demo.clients.base_api import BaseAPI
from dataflow_demo import utils
from dataflow_demo.utils import NotLoginError, check_login


class DataAPI(BaseAPI):
    def _create_client(self):
        client = DataSource.Client(self.protocol)
        return client

    @check_login
    def write_stock_tick(self, date, df):
        tick_table = UnversionedTable()
        tick_table.date = date
        tick_table.data = self._context.serialize(df).to_buffer().to_pybytes()
        self.client.write_stock_tick(table=tick_table)

    @check_login
    def read_stock_tick(self, date):
        response = self.client.read_stock_tick(date=date)
        tick_df = self._context.deserialize(response.data)
        return tick_df
    
    @check_login
    def write_stock_daily(self, date, df, comment=''):
        daily_table = VersionedTable()
        daily_table.date = date
        daily_table.data = self._context.serialize(df).to_buffer().to_pybytes()
        daily_table.timestamp = time.time()
        daily_table.user = self.username
        daily_table.comment = comment
        self.client.write_stock_daily(table=daily_table)
    
    @check_login
    def read_stock_daily(self, date):
        response = self.client.read_stock_daily(date=date)
        daily_df = self._context.deserialize(response.data)
        return daily_df
    
    @check_login
    def write_signal(self, date, df, sig_type, comment=''):
        signal_table = VersionedTable()
        signal_table.date = date
        signal_table.data = self._context.serialize(df).to_buffer().to_pybytes()
        signal_table.timestamp = time.time()
        signal_table.user = self.username
        signal_table.comment = comment
        signal_table.sig_type = sig_type
        self.client.write_signal(table=signal_table)
    
    @check_login
    def read_signal(self, date, sig_type):
        response = self.client.read_signal(date=date, sig_type=sig_type)
        signal_df = self._context.deserialize(response.data)
        return signal_df
    

if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]
    print('Connecting to %s:%s' % (host, port))

    tick_df = utils.build_dummy_tick_table()
    daily_df = utils.build_dummy_daily_table()
    signal_df = utils.build_dummy_signal_table()

    api = DataAPI(host, int(port))
    api.authenticate('zhuoshi', 'zhuoshi')

    print('Testing read/write stock tick')
    api.write_stock_tick('20200418', tick_df)
    read_tick_df = api.read_stock_tick('20200418')
    assert read_tick_df.equals(tick_df)

    print('Testing read/write stock daily')
    api.write_stock_daily('20200418', daily_df, 'api demo')
    read_daily_df = api.read_stock_daily('20200418')
    assert read_daily_df.equals(daily_df)

    print('Testing read/write signal')
    api.write_signal('20200418', signal_df, sig_type='demo_sig')
    read_signal_df = api.read_signal('20200418', sig_type='demo_sig')
    print('Passed all tests.')
