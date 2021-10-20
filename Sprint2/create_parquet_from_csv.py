#! /usr/bin/env python3

# Created by Zihang Jiang on 2021/10/17.
# Copyright © 2021 Zihang Jiang. All rights reserved.

import glob
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import time
from datetime import date


# Method one: using df.to_parquet to convert dataframe to parquet
# this method can't control row group number
files = glob.glob("./turnstile_csv/turnstile*.csv")

def read_csv(filename):
    return pd.read_csv(
        filename,
        parse_dates=["DATE"],
        infer_datetime_format=True,
    )
dfs = list(map(read_csv, files))
df = pd.concat(dfs)
df.to_parquet("./turnstile_parquet/turnstile.parquet")
# df.to_csv("turnstile_15_to_21.csv", index=False)


# Method two: convert dataframe to pyarrow table, then using ParquetWriter convert table to parquet
# this method can manually control row group number and content
years = range(15,22)

def read_csv_by_year(year):
    files_by_year = glob.glob(f"./turnstile_csv/turnstile{year}*.csv")
    dfs = list(map(read_csv, files_by_year))
    return pd.concat(dfs)

dfs = list(map(read_csv_by_year, years))

table = pa.Table.from_pandas(dfs[0], preserve_index=False)
writer = pq.ParquetWriter('./turnstile_parquet/turnstile_by_year.parquet', table.schema)

for df in dfs:
    table = pa.Table.from_pandas(df, preserve_index=False)
    writer.write_table(table)
writer.close()