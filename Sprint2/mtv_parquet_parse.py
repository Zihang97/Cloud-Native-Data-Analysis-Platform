#! /usr/bin/env python3

# Created by Zihang Jiang on 2021/10/17.
# Copyright © 2021 Zihang Jiang. All rights reserved.

import glob
import pandas as pd
import pyarrow.parquet as pq
import time
from datetime import date

filename = "./turnstile_parquet/turnstile_by_year.parquet"
pq_file = pq.ParquetFile(filename)

overview = [{"columns": pq_file.metadata.num_columns,
                        "rows": pq_file.metadata.num_rows,
                        "row_groups": pq_file.metadata.num_row_groups}
                        ]

overview_df = pd.DataFrame(overview)
print(overview_df.to_string(index=False))
print()

def sizeof_fmt(size, decimal_places=2):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
        if size < 1024.0 or unit == 'PiB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

print(pq_file.metadata.schema)
print()

group_info = []
for rg in range(pq_file.metadata.num_row_groups):
    dict = {}
    column = 6 # DATE
    rg_meta = pq_file.metadata.row_group(rg)
    dict["num_rows"] = rg_meta.num_rows
    dict["size"] = sizeof_fmt(rg_meta.total_byte_size)
    dict["min"] = rg_meta.column(column).statistics.min
    dict["max"] = rg_meta.column(column).statistics.max
    group_info.append(dict)
group_info_df = pd.DataFrame(group_info)
print(group_info_df)
print()

rg_meta = pq_file.metadata.row_group(3)
print(rg_meta.column(6))
print()
