# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 15:29:33 2014

@author: Anshumaan
"""


## This is a script for problem 12 in project euler. The aim is to find the
## triangular number which has 500 divisors.

import all_factors as af


def triangular_no(n):  # gives nth triangular number
    return sum(range(1, n + 1))

n = 1

while len(af.all_factors(triangular_no(n))) < 498:  # Number of divisors
    n += 1
print n


## I check only till 498 because the function all factors fives only the
## factors and doesn't include 1 and the number itself
