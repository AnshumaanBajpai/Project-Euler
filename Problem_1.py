# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 20:25:18 2014

@author: Anshumaan
"""


## This script is the solution to Problem 1 in project Euler.


import numpy as np
from fractions import gcd


## The function takes three inputs: The numbers whose multiples are to be
## added and the maximum limit.


def mult(n1, n2, Max):
    n3 = (n1 * n2) / gcd(n1, n2)
    return (sum(np.arange(n1, Max, n1)) + sum(np.arange(n2, Max, n2)) -
            sum(np.arange(n3, Max, n3)))


## Specific case of Project Euler.


print mult(3, 5, 1000)

