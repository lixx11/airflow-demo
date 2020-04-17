#!/usr/bin/env python

import os
import sys
import glob
import time
import pandas as pd
import pyarrow as pa

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dataflow_demo.servers.data_source_rpc import DataSource
from dataflow_demo.servers.data_source_rpc.ttypes import (
    VersionedTable,
    UnversionedTable,
)


def build_dummy_daily_table():
    n = 100
    df = pd.DataFrame({
        'code': ['600001.SSE'] * n,
        'date': ['20200101'] * n,
        'low': [10.] * n,
        'high': [12.] * n,
        'open': [11.] * n,
        'close': [11.] * n,
    })
    return df


def build_dummy_tick_table():
    n = 100
    df = pd.DataFrame({
        'datetime': ['20200101-09:30:00'] * n,
        'code': ['600001.SSE'] * n,
        'lastprice': [10.1] * n,
        'bidprice': [10.1] * n,
        'askprice': [10.1] * n,
        'volume': [10000] * n,
    })
    return df


def main():
    transport = TSocket.TSocket('localhost', 10000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = DataSource.Client(protocol)
    transport.open()

    context = pa.default_serialization_context()
    # write stock tick
    print('Testing write stock tick')
    tick_table = UnversionedTable()
    tick_table.date = '20200416'
    tick_df = build_dummy_tick_table()
    tick_table.data = context.serialize(tick_df).to_buffer().to_pybytes()
    client.write_stock_tick(table=tick_table)
    # read stock tick
    print('Testing read stock tick')
    response = client.read_stock_tick(date='20200416')
    df = context.deserialize(response.data)
    print(df.head())
    # write stock daily
    print('Testing write stock daily')
    daily_table = VersionedTable()
    daily_table.date = '20200416'
    daily_df = build_dummy_daily_table()
    daily_table.data = context.serialize(daily_df).to_buffer().to_pybytes()
    daily_table.timestamp = time.time()
    daily_table.user = 'zhuoshi'
    daily_table.comment = 'demo'
    client.write_stock_daily(table=daily_table)
    # read stock daily
    print('Testing read stock daily')
    response = client.read_stock_daily(date='20200416')
    df = context.deserialize(response.data)
    print(df.head())
    transport.close()


if __name__ == '__main__':
    main()
