# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 21:27:54 2014

@author: Anshumaan
"""

## This is a brute force script to find all the factors (composite and prime)
## of any given number.

import math


def all_factors(n):
    i = 2
    factors = []
    while i < int(math.sqrt(n)) + 1:
        if n % i == 0:
            factors += [i, n/i]
        i += 1
    return sorted(factors)
