# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:44:03 2019

@author: marjan
"""

import numpy as np


input_data = input().rstrip().split()
## given two interger array N*P and M*P

n = int(input_data[0]) #row
m = int(input_data[1]) #row
p = int(input_data[2]) #column

n_list = []
for _ in range (n):
    n_row = input()
    n_row = [int(x) for x in n_row.split()]
    n_list.append(n_row)
    
n_array = np.array(n_list)

m_list = []
for _ in range(m):
    m_row = input()
    m_row = [int(x) for x in m_row.split()]
    m_list.append(m_row)
    
m_array = np.array(m_list)
print(np.concatenate((n_array, m_array), axis = 0))  