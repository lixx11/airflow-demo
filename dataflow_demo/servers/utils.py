#!/usr/bin/env python

from sqlalchemy import create_engine
import pymongo
from pprint import pprint


def init_db(db_conf):
    my_db, mg_db = {}, {}
    # mysql databases
    my_conf = db_conf['mysql']
    user = my_conf['user']
    host = my_conf['host']
    port = my_conf['port']
    password = my_conf['password']
    for database in my_conf['databases']:
        my_db[database] = create_engine(
            f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
        ).connect()
    # mongodb collections
    mg_conf = db_conf['mongodb']
    host = mg_conf['host']
    port = mg_conf['port']
    mg_client = pymongo.MongoClient(host=host, port=port)
    for database in mg_conf['databases']:
        db_name = database['name']
        _mg_db = mg_client[db_name]
        mg_db[db_name] = {}
        for collection in database['collections']:
            mg_db[db_name][collection] = _mg_db[collection]
    return my_db, mg_db
