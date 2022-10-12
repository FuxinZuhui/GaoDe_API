#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/12 17:02
# @Author  : tvhead98
# @File    : get_geographic_info.py

import requests
import json
from const import *

def get_poi_district(a):
    url = 'https://restapi.amap.com/v3/geocode/regeo?parameters'  # 高德路径规划API
    params = {'key': GAODE_KEY,
              'location': a,  # 起点坐标， 经度，维度
              'extensions': 'all'
              }

    res = requests.get(url, params)
    jd = json.loads(res.text)  # 将数据由json格式转为Python字典
    district = jd['regeocode']['addressComponent']['district']
    return district

def get_shortest_driving_time(a, b):
    '''返回a到b的驾驶距离,其中a、b格式为经纬度'''
    url2 = 'https://restapi.amap.com/v3/direction/driving?parameters'  # 高德路径规划API
    params = {'key': GAODE_KEY,
              'origin': a,  # 起点坐标， 经度，维度
              'destination': b,  # 终点坐标
              'extensions': 'all',
              'strategy': 0, # 速度优先，时间最短
              }

    res = requests.get(url2, params)
    jd = json.loads(res.text)  # 将数据由json格式转为Python字典
    time = jd['route']['paths'][0]['duration']
    taxi_cost = jd['route']['taxi_cost']
    return int(time), int(taxi_cost)

def get_shortest_driving_path(a, b):
    '''返回a到b的驾驶距离,其中a、b格式为经纬度'''
    url2 = 'https://restapi.amap.com/v3/direction/driving?parameters'  # 高德路径规划API
    params = {'key': GAODE_KEY,
              'origin': a,  # 起点坐标， 经度，维度
              'destination': b,  # 终点坐标
              'extensions': 'all',
              'strategy': 2, # 距离优先，路径最短
              }

    res = requests.get(url2, params)
    jd = json.loads(res.text)  # 将数据由json格式转为Python字典
    distance = jd['route']['paths'][0]['distance']
    taxi_cost = jd['route']['taxi_cost']
    return int(distance), int(taxi_cost)