# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 18:41:03 2014

@author: Anshumaan
"""


## This is a solution to problem 20 in project_euler. The aim is to calculate
## the sum of digits for the factorial of a given number.


def factorial(n):  # calculates the factorial of a given number
    return reduce(lambda x, y: x * y, range(1, n+1))


n = 100


f_n = factorial(n)  # calculates the factorial of n and saves in f_n


print reduce(lambda x, y: x + y, [int(str(f_n)[i]) for i
             in range(len(str(f_n)))])  # calculates the sum of all digits
