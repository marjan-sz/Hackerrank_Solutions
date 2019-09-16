# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:28:54 2019

@author: marjan
"""

def is_leap(year):
    leap = False

    if (year % 4 == 0) and (year % 100 != 0) and (year % 400 != 0):
        leap = True
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 != 0):
        leap = False
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        leap = True

    return leap

year = int(input())
print(is_leap(year))