# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 22:21:25 2014

@author: Anshumaan
"""


## This is a script for the problem 22 in project_euler.


with open("p022_names.txt") as names:
    for line in names:
        namelist = line.split(",")
    namelist = [i[1:-1] for i in sorted(namelist)]  # sorting alphabetically
    sumed_list = [sum([ord(a[i]) - 64 for i in range(len(a))]) for a in
                  namelist]  # creating a list with sum of term characters

## Now we multiply the index of each term with the term in the sumed_list.

    print sum([sumed_list[i] * (i + 1) for i in range(len(sumed_list))])
