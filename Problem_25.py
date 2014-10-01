# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 22:07:22 2014

@author: Anshumaan
"""

## This is the script for problem 25 in Project Euler. The first function is
## just a basic function to generate nth fibonacci number and is not
## necessarily needed for the problem


def fibonacci(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibo = [1, 1]

count = 2
while (len(str(fibo[1])) < 1000):
    fibo = [fibo[1], fibo[0] + fibo[1]]
    count += 1


print count
