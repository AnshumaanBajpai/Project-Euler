# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 12:43:19 2014

@author: Anshumaan
"""


## This is a script for problem 7 in Euler_project. The aim is to find out the
## 100001st prime number.


import is_prime_small as ips


def nth_prime(n):  # defining a function to calculate the nth prime
    p = [2]
    i = 3
    while len(p) < n:
        if ips.isprime(i):
            p.append(i)
        i += 2
    return p[-1]
