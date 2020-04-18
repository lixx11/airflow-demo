import pandas as pd


def build_dummy_daily_table(n=100):
    df = pd.DataFrame({
        'code': ['600001.SSE'] * n,
        'date': ['20200101'] * n,
        'low': [10.] * n,
        'high': [12.] * n,
        'open': [11.] * n,
        'close': [11.] * n,
    })
    return df


def build_dummy_tick_table(n=100):
    df = pd.DataFrame({
        'datetime': ['20200101-09:30:00'] * n,
        'code': ['600001.SSE'] * n,
        'lastprice': [10.1] * n,
        'bidprice': [10.1] * n,
        'askprice': [10.1] * n,
        'volume': [10000] * n,
    })
    return df


def build_dummy_signal_table(n=100):
    df = pd.DataFrame({
        'code': ['600001.SSE'] * n,
        'date': ['20200101'] * n,
        'low': [10.] * n,
        'high': [12.] * n,
        'open': [11.] * n,
        'close': [11.] * n,
        'signal': [666] * n,
    })
    return df


class NotLoginError(Exception):
    pass


def check_login(func):
    def wrapper(self, *args, **kargs):
        if self.is_login():
            return func(self, *args, **kargs)
        else:
            raise NotLoginError('Not login yet!')
    return wrapper
