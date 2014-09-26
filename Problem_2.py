# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 21:08:07 2014

@author: Anshumaan
"""

## This is a solution to problem 2 from Project_Euler


## This is a function to generate fibonacci series upto the given maximum.


def fibonacci(n):
    fib_list = []
    if n == 1:
        fib_list += [1]
    elif n == 2:
        fib_list += [1, 2]
    else:
        fib_list += [1, 2]
        i = 1  # index of the last number in the fibonacci series so far.
        while fib_list[i] < n:
            fib_list += [fib_list[i] + fib_list[i-1]]
            i += 1
    if fib_list[-1] == n:
        return fib_list
    else:
        return fib_list[:-1]


fibonacci_list = fibonacci(4000000)


## calculating the sum of even numbers in the list

print sum(x for x in fibonacci_list if x % 2 == 0)
