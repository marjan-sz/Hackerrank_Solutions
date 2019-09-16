# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:58:51 2019

@author: marjan
"""

import numpy as np



input_data = input().rstrip().split()

n = int(input_data[0])
m = int(input_data[1])
my_array = [] #np.empty([n, m])

for _ in range (n):
    row = input()
    row = [int(x) for x in row.split()]
    my_array.append(row)
 
## covert a list of lists to a numpy array
my_array = np.array(my_array)
print("Transposed array: ", np.transpose(my_array))
print("Flatten array: ", my_array.flatten())
   