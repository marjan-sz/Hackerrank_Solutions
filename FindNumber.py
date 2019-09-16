# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:45:47 2019

@author: marjan
"""

#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def findNumber(arr, k):
    if k in arr:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    #fptr = open(os.environ['/home/marjan/practise/hackerrank/output.txt'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)
    
    

    #fptr.write(res + '\n')

    #fptr.close()
