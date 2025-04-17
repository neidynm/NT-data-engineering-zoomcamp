#!/usr/bin/env python
# coding: utf-8
import argparse
from time import time
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import sqlalchemy as sqla
import pyarrow.parquet as pq
import pyarrow as pa
import os
from urllib.parse import urlparse

## Main function
def main():
    user = os.environ.get("user")
    password = os.environ.get("password")
    host = os.environ.get("host")
    port = os.environ.get("port")
    db = os.environ.get("db")
    table_name = os.environ.get("table_name")
    url = os.environ.get("url")
    print ('I am printing the URL: '+url)

    csv_name = 'yellow_tripdata_2021-01.parquet'

    #download Parquet file
    os.system(f"curl -O {url}")
    path = urlparse(url).path
    parquet_file_path = f"./{os.path.basename(path)}"
    pf = pq.ParquetFile(parquet_file_path)
    
    #connect to the database
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    with engine.begin() as conn:
        conn.execute(sqla.text(f"""DROP Table IF exists {table_name}"""))

    #sql.execute('DROP Table IF exists %s'%table_name, engine)

    for i in pf.iter_batches(batch_size= 10000):
        t_start = time()
        df= i.to_pandas()
        df.to_sql(name=table_name, con = engine, if_exists = 'append')
        t_end = time()
        print('Inserted another chunk, took %.3f second' %(t_end - t_start))

if __name__ =='__main__':
    main() 