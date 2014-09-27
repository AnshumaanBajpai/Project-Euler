# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 23:33:15 2014

@author: Anshumaan
"""


## This script is a solution to problem 4 on project Euler. n1 is the starting
## natural number and n2 is the neding natural number.


import math


def diff(n1, n2):
    square_sum = math.pow(sum(range(n1, n2 + 1)), 2)
    print range(n1, n2 + 1)
    sum_square = sum([i*i for i in range(n1, n2 + 1)])
    return int(square_sum - sum_square)


## We can also use the formula (n*(n + 1)/2) and n*(n + 1)*(2n + 1)/6 which
## will give the desired results for first n numbers but I have tried to get
## the answer for any given range. The following script does the more specific
## case of the exact problem given to us.


def diff_formula(n):
    square_sum = math.pow(n * (n + 1) / 2, 2)
    sum_square = n * (n + 1) * (2 * n + 1) / 6
    return int(square_sum - sum_square)
