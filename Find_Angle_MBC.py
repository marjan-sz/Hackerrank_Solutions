# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:57:52 2019

@author: marjan
"""

import math




if __name__ == '__main__':
    
    ab = float(input("Insert AB lenght: "))
    bc = float(input("Insert BC lenght: "))
    
    """
    (ac)^2 = (ab)^2 + (bc)^2
    ac = sqrt((ac)^2)
    mc = ac/2
    sin(theta) = mc/bc
    theta = arcsin(mc/bc)
    """
    ac = math.sqrt(pow(ab, 2) + pow(bc, 2))
    mc = ac/2
    try:
        theta_radian = math.asin(mc/bc)
    except ValueError:
        if (mc/bc) > 0 :
            theta_radian = math.asin(math.floor(mc/bc))
        elif (mc/bc) < 0 :
            theta_radian = math.asin(math.ceil(mc/bc))
    ## radian to degree
    theta_degree = math.degrees(theta_radian)
    print(str(theta_degree) + "\xb0")