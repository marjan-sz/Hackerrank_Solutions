# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:25:18 2019

@author: marjan
"""

import math
import os
import random
import re
import sys
import itertools


def replace_non_alphanumerics(myStr):
    """
    Remove symbols or spaces between two alphanumeric characters\
    and replace it with a space
    """
    
    ## pattern to find non-alphanumerics chars between two alphanumeric chars
    p = re.compile(r'\w\W+\w')
    ## find all substring having the pattern
    tmp = p.findall(myStr)
    ## add '\' to escape special characters such as $, therwise it will be assumed as end of the string
    tmp = [re.escape(x) for x in tmp]
    ## for all found patterns, remove non-alphanumeric characters and replace it with found patterns
    for x in tmp:
        y = re.sub(r'\W+', ' ', x)
        myStr = re.sub(x, y, myStr)
 
    return myStr
    

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix_item = ','.join(matrix_item).split(',')
    matrix.append(matrix_item)
    
columnwise_matrix = list(zip(*matrix))
flat_list = list(itertools.chain(*columnwise_matrix))
str_list = ''.join(flat_list)
print(replace_non_alphanumerics(str_list))


