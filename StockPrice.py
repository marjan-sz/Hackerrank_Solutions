# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:37:47 2019

@author: marjan
"""
import calendar
from datetime import date
import time
import pandas as pd
import requests
import json

def convert_date(x):
    
    month_dict = {'January': 1, 'February': 2, 'March':3, 'April': 4, 'May': 5, 'June':6, 'July':7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December':12}
    d = x.split('-')
    d = [int(d[0]), int(month_dict[d[1]]), int(d[2])]
    d = d[::-1]
    mydate = date(d[0], d[1], d[2])
    return mydate


def check_conds(x, firstDateS, lastDateS, weekDay):
    
    date = convert_date(x['date'])
    weekday = calendar.day_name[date.weekday()]
    if (date > firstDateS) and (date < lastDateS) and (weekday == weekDay):
        print(' '.join([str(x['date']), str(x['open']), str(x['close'])]))

    

def  openAndClosePrices(firstDate, lastDate, weekDay):
    
    firstDateS = convert_date(firstDate)
    lastDateS = convert_date(lastDate)
    
    start_year = firstDateS.year
    end_year = lastDateS.year
    year_tmp = [x for x in range (start_year, end_year+1)]
    page_tmp = [z for z in range(1, 6)]
    
    
    session = requests.Session()
    session.trust_env = False
    
    res = []
    for y in year_tmp:
        for p in page_tmp:
            url = 'https://jsonmock.hackerrank.com/api/stocks/search?date='+ str(y) + '&page=' + str(p)
            if session.get(url, stream= True).json()['data']!= []:
                res.append(session.get(url, stream= True).json()['data'])
    
    data_df = pd.DataFrame.from_dict(res[0])
    data_df.apply(lambda x: check_conds(x, firstDateS, lastDateS, weekDay), axis = 1)
            



start_time = time.time()
try:
    _firstDate = str(input())
except:
    _firstDate = None


try:
    _lastDate = str(input())
except:
    _lastDate = None


try:
    _weekDay = str(input())
except:
    _weekDay = None
    


openAndClosePrices(_firstDate, _lastDate, _weekDay)
print("Time spent in seconds: ", time.time() - start_time)