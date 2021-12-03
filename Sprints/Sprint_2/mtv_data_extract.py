#! /usr/bin/env python3

# Created by Zihang Jiang on 2021/10/16.
# Copyright © 2021 Zihang Jiang. All rights reserved.

import requests
import pandas as pd

original_url = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_'

# response = requests.get(url)
# lines = response.text.splitlines()
for year in range(10, 21):
	for month in range(1, 13):
		for day in range(1, 32):
			year, month, day = str(year), str(month), str(day)
			if len(month) < 2:
				month = '0' + month
			if len(day) < 2:
				day = '0' + day
			try:
				mtv_df = pd.read_csv(original_url + year + month + day + '.txt')
				mtv_df.columns = ['EXITS' if x=='EXITS                                                               ' else x for x in mtv_df.columns]
				mtv_df.to_csv(f'./turnstile_csv/turnstile{year}{month}{day}.csv', index = False)
			except:
				continue