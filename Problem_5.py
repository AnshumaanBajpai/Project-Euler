# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 19:28:49 2014

@author: Anshumaan
"""

## This script is for problem 5 in project Euler. The aim is to find out the
## least common multiple of natural number till 20. The way I am approaching
## this problem is by observing that the LCM from 11 to 20 will be a multiple
## natural numbers till 10.

import math
import is_prime_small as ips


## I first define a function that factorizes the given number into its prime
## factors

def all_prime_factors(n):
    i = 2
    factors = []
    while i < int(math.sqrt(n)) + 1:
        if (n % i) == 0:
            if ips.isprime(n / i):
                factors += [i, n/i]
            else:
                factors += [i]
            n = n/i
            i = 1
        i += 1
    return sorted(factors)


def lcm(low_lim, up_lim):
    number_list = range(low_lim + 1, up_lim + 1)  # Numbers whose lcm is needed
    lcm_i = low_lim  # By default includes the first number of the list
    for i in range(len(number_list)):
        if ips.isprime(number_list[i]):  # if prime, it is multiplied to lcm_i
            lcm_i = lcm_i * number_list[i]
        test = all_prime_factors(number_list[i])  # if !prime, go through all
        nsf = 1  # acronym for number
        for j in range(len(test)):
            nsf = nsf * test[j]
            if (lcm_i % nsf) != 0:
                lcm_i = lcm_i * test[j]
    return lcm_i
