#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:58:06 2019

@author: marjan
"""
import time


def fib(n):
    
    """
    A recurrence formula that can be used to find nth Fibonacci number
    If n is even then k = n/2:
    F(n) = [2*F(k-1) + F(k)]*F(k)
    
    If n is odd then k = (n + 1)/2
    F(n) = F(k)*F(k) + F(k-1)*F(k-1)
    """
    ## create an array for memoization
    f = [0] * (n+1)
	# Base cases 
    if (n == 0) : 
        return 0
    if (n == 1 or n == 2) : 
        f[n] = 1
        return (f[n]) 

	# If fib(n) is already computed 
    if (f[n]) : 
        return f[n] 
    ## If n is odd
    ## convert n to binary and do bitwise 'and' operation with '0001'
    ## if the result is 1 means n is odd, otherwise it is even
    if( n & 1) :  
        k = (n + 1) // 2
    ## If n is even
    else :  
        k = n // 2

	# Applyting above formula 
    if((n & 1) ) : 
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
    else: 
        f[n] = (2*fib(k-1) + fib(k))*fib(k) 

    return f[n] 
    

if __name__ == '__main__':
    
    start_time = time.time()
    n = int(input("Insert n: "))
    print(fib(9))
    print("Time spent in seconds: ", time.time() - start_time)
    ## time complexity is O(lgn)