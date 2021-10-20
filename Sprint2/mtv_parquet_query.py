#! /usr/bin/env python3

# Created by Zihang Jiang on 2021/10/17.
# Copyright © 2021 Zihang Jiang. All rights reserved.

import glob
import pandas as pd
import pyarrow.parquet as pq
import pyarrow.csv as csv
import time
from datetime import date
import pyarrow.compute as pc

filename = "./turnstile_parquet/turnstile_by_year.parquet"

# Query "DATE" column
start = time.time()
table = pq.read_table(filename, filters=[("DATE", "=", date(2020,2,1))])
end = time.time()
print("It takes", end-start, "seconds to read and query the parquet file")
print(table.to_pandas())
print()



# Query column not "DATE"
start = time.time()
table = pq.read_table(filename, filters=[("ENTRIES", "=", 7364079)])
end = time.time()
print("It takes", end-start, "seconds to read and query the parquet file")
print(table.to_pandas())
print()


# Converting csv file to pyarrow table then filter
# start = time.time()
# table = csv.read_csv("turnstile_15_to_21.csv")
# end = time.time()
# print(end-start)

# date_value = table.column('DATE')
# row_mask = pc.equal(date_value, date(2020,2,1))
# start = time.time()
# selected_table = table.filter(row_mask)
# end = time.time()
# print(end-start)
# print(selected_table.to_pandas())


# Converting csv file to dataframe then query
# start = time.time()
# df = pd.read_csv("turnstile_15_to_21.csv", parse_dates=["DATE"], infer_datetime_format=True,)
# end = time.time()
# print("It takes", end-start, "seconds to read the csv file")

# start = time.time()
# print(df[(df["DATE"].dt.year == 2020) & (df["DATE"].dt.month == 2) & (df["DATE"].dt.day == 1)])
# end = time.time()
# print("It takes", end-start, "seconds to get querying result")