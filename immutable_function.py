#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:57:15 2019

@author: marjan
"""
import ast

#Original List = ['one', 'two', 'three']
#Add List = ['one', 'two', 'five', 'six']
#Delete List = ['two', 'five']
#Result List = ['three', 'six', 'one'] 


def func(original_tuple, add_tuple, delete_tuple):
    """
    Merge original tuple with add and delete tuples and order them
    Only tuples can be accepted as input arguments to have an immutable function
    in: three tuples f strs
    out: a tuple of strs
    """
    ## check the input data type to be tuples (which is immutable)
    if not(isinstance(original_tuple, tuple)):
        raise TypeError
    if not(isinstance(add_tuple, tuple)):
        raise TypeError
    if not(isinstance(delete_tuple, tuple)):
        raise TypeError
    
 
    ## add second list
    T = original_tuple
    for item in add_tuple:
        if item not in T:
            T = T + (item,)
    ## remove third list
    for item in T:
       if item in delete_tuple:
           index = T.index(item)
           T = T[:index] + T[index+1:]
           
    ## order elements    
    ## make a list of lists based on string lengths
    tmp1 = [len(x) for x in T]
    tmp3 = []
    for y in list(set(tmp1)):
        tmp2 = []
        for x in list(T):
            if (len(x) == y) and (x not in tmp2):
                tmp2.append(x)
                tmp2 = sorted(tmp2, reverse=True)
        tmp3.append(tmp2)
    tmp4 = sorted(tmp3, key=lambda t: [len(x) for x in t], reverse=True)
    ## make a flat list
    res = [item for sublist in tmp4 for item in sublist] 
        
    return res

if __name__ == '__main__':

    original_tuple = tuple(ast.literal_eval(input("Insert original list: ")))
    add_tuple = tuple(ast.literal_eval(input("Insert add list: ")))
    delete_tuple = tuple(ast.literal_eval(input("Insert delete list: ")))
        
    res = func(original_tuple, add_tuple, delete_tuple)
    print(res)

