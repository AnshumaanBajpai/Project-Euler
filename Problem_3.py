# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 21:27:54 2014

@author: Anshumaan
"""

## This is a solution to problem 3 in project_euler. The script uses the other
## scripts named is_prime_small.py and and all_factors.


import is_prime_small as ips
import all_factors as af


def prime_factors(n):
    factors = af.all_factors(n)  # Finds all the factors using all_factors.py
    return [i for i in factors if ips.isprime(i)]  # returns only the primes


print(prime_factors(600851475143L)[-1])
