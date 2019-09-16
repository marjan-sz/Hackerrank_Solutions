# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:09:43 2019

@author: marjan
"""

import math
import os
import random
import re
import sys

def n_weird_or_notweird(n):
    """
    This function gets n and return a string based on its value
    in: n is a positive integer within [1, 100] range
    out: a message as a string
    """
    if (n % 2 != 0): ## odd numbers
        print("weird")
    elif (n % 2 ==0) and (2 <= n <= 5):
        print("not weird")
    elif (n % 2 ==0) and (6 <= n <= 20):
        print("weird")
    elif (n % 2 ==0) and (n > 20):
        print("Not weird")



if __name__ == '__main__':
    n = int(input("Enter a positive integer number: "))
    n_weird_or_notweird(n)
    