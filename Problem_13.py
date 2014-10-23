# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 21:37:01 2014

@author: Anshumaan
"""

## This script is a solution to problem 13 in project Euler. In this I have to
## find the first 10 digits of a large sum of 100 fifty digit numbers.


## Importing the data and storing it as a grid

data = []
with open("Problem_13_data.txt") as p11:
    data += [long(line) for line in p11]

## data collected and saved

a = str(sum(data))  # summing up all the numbers stored in data
print a[0:10]  # finding out the first 10 digits in the sum
