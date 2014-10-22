# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 19:57:34 2014

@author: Anshumaan
"""


## This script is the solution to problem 18 in project euler.

triangle = []  # initialize the data as triangle

with open("Problem_18_data.txt") as data:
    for line in data:
        tmp = [int(i) for i in line.split()]
        triangle.append(tmp)


## Solving the problem now

i = len(triangle) - 1  # This is to track till the 2nd last line of triangle
bot_line = triangle[-1]  # The base of triangle which is iterated


## I use the bottom up approach to reduce the no. of calculations
while i > 0:
    tmp_bot = []
    for j in range(len(triangle[i]) - 1):
        tmp_bot.append(max([bot_line[j], bot_line[j+1]]) + triangle[i-1][j])
    bot_line = tmp_bot
    i -= 1

print bot_line
