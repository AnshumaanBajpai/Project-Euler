# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 16:09:19 2014

@author: Anshumaan
"""

## This is script is the exhaustive test for primality which can be useful for
## numbers of reasonable size.


import math


def isprime(n):
    if n == 2:
        return True
    elif n < 2 or (n % 2) == 0:
        return False
    else:
        return all(n % i for i in xrange(3, int(math.sqrt(n)) + 1, 2))
