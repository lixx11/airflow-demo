#!/usr/bin/env python
"""APIs for data server.
"""


import time
import sys
import pandas as pd

from thrift.Thrift import TApplicationException

from dataflow_demo.servers.data_server.data_source_rpc import DataSource
from dataflow_demo.servers.data_server.data_source_rpc.ttypes import (
    VersionedTable,
    UnversionedTable,
)

from dataflow_demo.clients.base_api import BaseAPI
from dataflow_demo import utils
from dataflow_demo.utils import NotLoginError, check_login, check_rpc


class DataAPI(BaseAPI):
    def _create_client(self):
        client = DataSource.Client(self.protocol)
        return client

    @check_rpc
    @check_login
    def write_stock_tick(self, date, df):
        """Write stock tick ``df`` on ``date`` to data server.

        Parameters
        ----------
        date : string
            date in %Y%m%d format, e.g. 20200418.
        df : pd.DataFrame
            stock tick dataframe, columns are defined in ``Notes`` section.

        Returns
        -------
        None

        Examples
        --------

        >>> api = dataflow_demo.clients.data_api.DataAPI(data_host, data_port)
        >>> api.authenticate(username, password, auth_host, auth_port)
        >>> api.write_stock_tick(date, df)

        Notes
        -----
        tick dataframe format

        =====  ===========  ===========  ======  ==========  ===================
        index  Column Name  Description  Type    Example     Comment
        =====  ===========  ===========  ======  ==========  ===================
        1      datetime     日期         str     20190920    SSE(上海)/SZE(深圳)
        2      code         股票代码     str     600000.SSE  
        3      lastprice    最新价格     double  10.22       
        4      bidprice     卖价         double  10.22      
        5      askprice     买价         double  10.22         
        6      volume       成交量       int     20         
        =====  ===========  ===========  ======  ==========  ===================
        """
        tick_table = UnversionedTable()
        tick_table.date = date
        tick_table.data = self._context.serialize(df).to_buffer().to_pybytes()
        self.client.write_stock_tick(self.token, tick_table)

    @check_rpc
    @check_login
    def read_stock_tick(self, date):
        response = self.client.read_stock_tick(self.token, date)
        tick_df = self._context.deserialize(response.data)
        return tick_df
    
    @check_rpc
    @check_login
    def write_stock_daily(self, date, df, comment=''):
        daily_table = VersionedTable()
        daily_table.date = date
        daily_table.data = self._context.serialize(df).to_buffer().to_pybytes()
        daily_table.timestamp = time.time()
        daily_table.user = self.username
        daily_table.comment = comment
        self.client.write_stock_daily(self.token, daily_table)
    
    @check_rpc
    @check_login
    def read_stock_daily(self, date):
        response = self.client.read_stock_daily(self.token, date)
        daily_df = self._context.deserialize(response.data)
        return daily_df
    
    @check_rpc
    @check_login
    def write_signal(self, date, df, sig_type, comment=''):
        signal_table = VersionedTable()
        signal_table.date = date
        signal_table.data = self._context.serialize(df).to_buffer().to_pybytes()
        signal_table.timestamp = time.time()
        signal_table.user = self.username
        signal_table.comment = comment
        signal_table.sig_type = sig_type
        self.client.write_signal(self.token, signal_table)
    
    @check_rpc
    @check_login
    def read_signal(self, date, sig_type):
        response = self.client.read_signal(self.token, date, sig_type)
        signal_df = self._context.deserialize(response.data)
        return signal_df
    

if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]
    auth_port = sys.argv[3]
    print(f'Connecting to {host}:{port} with auth port {auth_port}')

    tick_df = utils.build_dummy_tick_table()
    daily_df = utils.build_dummy_daily_table()
    signal_df = utils.build_dummy_signal_table()

    api = DataAPI(host, int(port))
    api.authenticate('zhuoshi', 'zhuoshi', host, auth_port)

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

    api.close()
