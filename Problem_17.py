# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 21:00:29 2014

@author: Anshumaan
"""


## This is a solution to problem 17 in project euler.


import num2word


letters = 0
for i in range(1, 1001):
    s = num2word.to_card(i)
    des_s = s.replace(" ", "").replace("-", "")
    letters += len(des_s)

print letters
