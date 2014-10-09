# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 15:03:18 2014

@author: Anshumaan
"""


## This script is a solution to Problem 10 in project_euler. The aim is to add
## the prime numbers upto 2 million


import is_prime_small as ips


sum_p = 2  # The sum of the prime numbers
p = 3

while p < 2000000:
    if ips.isprime(p):
        sum_p += p
    p += 2


print sum_p
