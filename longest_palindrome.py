#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:12:45 2020

@author: marjan

Question: Find the longest palindrome in a string

A) Redefining the question:
    palindrome is a word or phrase which reads the same as backward and forward
    given an input string, return the longest palindrome sub-string existing in the input string

B) Clarify all possible cases
    -> Return TypeError if the input is not a string
    -> Return space if the input is space
    -> What to do with special characters, numbers and punctuations? Remove them
    -> Shall we differentiate between upper and lower case letters? No, consider them all lower-case or all upper-case 
    -> What to do with spaces? Remove them
    
    
C) General steps to solve the problem
    1. check if the input is a string
    2. remove all space, special characters, numbers and convert them to lower case
    3. find all sub-strings from the input string
        a) create an array to save palindrome sub-strings, called pali_subs
        b) check each sub-string, if it is same backward and forward, add it to the pali_subs array
    4. find the maximum length sub-string in pali_subs and return it
    

D) Pseudocode
    1. if the input is a string else return error
    2. use regular expression to remove all non-alphabet characters from the string
    3. convert string characters to lower case with lower() built-in function
    4. find all sub-strings with a nested for loop
    5. create an array to save palindrome strings
    6. check each sub-string, if it is palindrome, save it in the array
    7. find sub-string lengths in the array and return the longest one

"""
import re

def longest_palindrome(a):
    
    ## check if the input is a string
    if not isinstance(a, str):
        return TypeError
    ## regular expression to remove non-alphabetic characters
    regex = re.compile('[^a-zA-Z]')
    ## remove regex from the string and convert to lower case
    input_str = regex.sub('', a).lower()
    ## find all sub-strings in the input string
    n = len(input_str)
    ## create an array to store palindrome sub-strings
    palindrome_subs = []
    for i in range(n):
        for j in range(i+1, n+1):
            tmp = input_str[i:j]
            if tmp == tmp[::-1]:
                palindrome_subs.append(tmp)
    ## find the longest sub-string in palindrome_subs      
    return(max(palindrome_subs, key=len))
    
                
    

a = "A Santa Lived As a Devil At NASA."
print(longest_palindrome(a))

