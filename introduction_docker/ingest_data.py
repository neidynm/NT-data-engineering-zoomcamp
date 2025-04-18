#!/usr/bin/env python
# coding: utf-8
import argparse
from time import time
from datetime import datetime
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import sqlalchemy as sqla
import pyarrow.parquet as pq
# import pyarrow as pa
import os
from urllib.parse import urlparse
import logging
import sys

timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
log_filename = f"logs/ingest_{timestamp}.log"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler(sys.stdout)
    ]
)

## Main function
def main():
    logging.info("Starting data ingestion...")

    user = os.environ.get("user")
    password = os.environ.get("password")
    host = os.environ.get("host")
    port = os.environ.get("port")
    db = os.environ.get("db")
    table_name = os.environ.get("table_name")
    url = os.environ.get("url")

    csv_name = 'yellow_tripdata_2021-01.parquet'
    try:
        #download Parquet file
        logging.info("Downloading the source data ...")
        os.system(f"curl -O {url}")
        path = urlparse(url).path
        parquet_file_path = f"./{os.path.basename(path)}"
        pf = pq.ParquetFile(parquet_file_path)
        
        #connect to the database

        logging.info("Connecting to the database ...")
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

        with engine.begin() as conn:
            conn.execute(sqla.text(f"""DROP Table IF exists {table_name}"""))

        for i in pf.iter_batches(batch_size= 10000):
            t_start = time()
            df= i.to_pandas()
            df.to_sql(name=table_name, con = engine, if_exists = 'append')
            t_end = time()
            logging.info('Inserted another chunk, took %.3f second' %(t_end - t_start))
    except Exception as e:
        logging.error("An error occurred during ingestion", exc_info=True)

if __name__ =='__main__':
    main() 