# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 21:27:54 2014

@author: Anshumaan
"""

## This is a brute force script to find the prime factors of a given number.


import is_prime_small as ips
import all_factors as af


def prime_factors(n):
    factors = af.all_factors(n)
    return [i for i in factors if ips.isprime(i)]
