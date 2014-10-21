# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 20:42:06 2014

@author: Anshumaan
"""

## This script is a solution to problem 4 in project euler. The aim is to find
## the largest pallindrome obtained by multiplying two 3-digit number.


## First we define a function to test if a number is palindrome.

def palin_test(n):
    number = str(n)
    palindrome = True
    for i in range(int(len(number) / 2)):
        if number[i] != number[len(number) - (i + 1)]:
            palindrome = False
            break
    return palindrome


## Now we check the products of all three digit numbers and test them.

palindrome_list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if ((i % 11) or (j % 11)) and palin_test(i * j):
            palindrome_list.append(i * j)

print max(palindrome_list)
