#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/13 12:30
# @Author  : tvhead98
# @File    : check_integrity.py.py

import json
from const import *
import pandas as pd
from get_geographic_info import *
import time

OUTPUT_FILE = './output_data/geographic_info.data.full'

routes_dict = {}
with open('./output_data/geographic_info.data', mode='r', encoding='utf8') as f:
    for line in f:
        line = line.strip('\n')
        if line == '':
            continue
        line = json.loads(line)
        ori = line['ori_name']
        des = line['des_name']
        routes_dict[(ori, des)] = line

district_dict = {}
with open('raw_data/district.data', mode='r', encoding='utf8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        district_dict[line[0]] = line[1]

missing_routes = set()
poi_list = pd.read_csv(POI_FILE)
poi_num = len(poi_list)
for o in range(79, poi_num):
    for d in range(o+1, poi_num):
        ori = poi_list.loc[o]
        des = poi_list.loc[d]
        ori_name = ori['attraction']
        des_name = des['attraction']
        if (ori_name, des_name) in routes_dict:
            continue
        print('find 1 missing route!')
        ori_pos = str(ori['lng']) + ',' + str(ori['lat'])
        des_pos = str(des['lng']) + ',' + str(des['lat'])
        ori_district = district_dict[ori_name]
        des_district = district_dict[des_name]
        shortest_driving_time, taxi_fee_1 = get_shortest_driving_time(ori_pos, des_pos)
        shortest_driving_path, taxi_fee_2 = get_shortest_driving_path(ori_pos, des_pos)
        texi_fee = min(taxi_fee_1, taxi_fee_2)
        data = {
            'ori_name': ori_name,
            'des_name': des_name,
            'ori_district': ori_district,
            'des_district': des_district,
            'shortest_driving_time': shortest_driving_time,
            'shortest_driving_path': shortest_driving_path,
            'texi_fee': texi_fee
        }
        routes_dict[(ori_name, des_name)] = data
        time.sleep(1)
    time.sleep(1)

print('checking done, routes dict len: ', len(routes_dict))

with open(OUTPUT_FILE, mode='w', encoding='utf8') as f:
    for key in routes_dict:
        data = routes_dict[key]
        data = json.dumps(data, ensure_ascii=False)
        f.write(data+'\n')

