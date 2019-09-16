# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:18:52 2019

@author: marjan
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
import itertools

#
# Complete the 'customSort' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def customSort(arr):
    #print("before change", arr)
    arr = sorted(arr)
    counter_dict = Counter(arr)
    
    values = list(counter_dict.values())
    res = []
    #print("after change", arr)
    for v in list(set(values)):
        item_freq = []
        #item_freq = [y for y in arr if counter_dict[y] == x]
        for y in arr:
            #print("in loop", arr)
            if counter_dict[y] == v:
                item_freq.append(y)
        res.append(item_freq)
    
#    if (any(isinstance(i, list) for i in res)):
    res = [sorted(x) for x in res]
    #res = list(itertools.chain.from_iterable(res))
    #print(res)
    res = [item for sublist in res for item in sublist]
#    else:
#        res = sorted(res)
#        pass
    res = list(map(str, res))

    print('\n'.join(res))
        
    
    

if __name__ == '__main__':
    import time
    start_time = time.time()
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    customSort(arr)
    print("Time spent in seconds: ", time.time() - start_time)
#    tmp = [str(x) for x in tmp]
#    print('\n\n')
#    print('\n'.join(tmp))
