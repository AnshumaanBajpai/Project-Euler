# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 21:27:54 2014

@author: Anshumaan
"""

## This is the solution for problem 4 in Project Euler. I am using the (n^0.5)
## concept to factorize the given number. The code needs to be fixed.

import math


def prime(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))
n = 600851475143L
#n = 35
i = 1

factors = []
while i < math.floor(math.sqrt(n)):
    if n % i == 0:
        n = n / i
        if prime(i):
            factors.append(i)
        if prime(n):
            factors.append(n)
    i = i + 1

factors = sorted(factors)
print factors

print prime(4)