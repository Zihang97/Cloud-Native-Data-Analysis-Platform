#! /usr/bin/env python3

# Created by Zihang Jiang on 2021/11/17.
# Copyright © 2021 Zihang Jiang. All rights reserved.

import glob
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import time
from datetime import date


# Method one: using df.to_parquet to convert dataframe to parquet
# this method can't control row group number
filefolder = input("please enter the folder name where you store txt files: ")
outfilefolder = input("please enter the name of parquet file you want to create: ")
files = glob.glob(filefolder)

def read_csv(filename):
    return pd.read_csv(
        filename,
        parse_dates=["DATE"],
        infer_datetime_format=True,
    )
dfs = list(map(read_csv, files))
df = pd.concat(dfs)
df.to_parquet(outfilefolder)