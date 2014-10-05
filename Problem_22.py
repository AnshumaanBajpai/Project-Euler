# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 22:21:25 2014

@author: Anshumaan
"""


## This is a script for the problem 22 in project_euler.


with open("p022_names.txt") as names:
    namelist = []
    print names
    for line in names:
        namelist += line.split(",")
    print len(sorted(namelist))
