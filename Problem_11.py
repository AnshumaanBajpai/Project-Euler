# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 20:52:01 2014

@author: Anshumaan
"""

## This script is a solution to problem 11 in project Euler. In this I have to
## calculate the maximum product of four number in a grid.


## Importing the data and storing it as a grid

data = []
with open("Problem_11_data.txt") as p11:
    for line in p11:
        data.append([int(i) for i in line.split()])

## data collected and saved

max_rows = []  # This will store the maximum product for each row.
max_column = []  # This will store the maximum product for each column
max_diag_right = []  # This will store the maximum product for diagonal_right
max_diag_left = []  # This will store the maximum product for diagonal_left

for i in range(len(data)):
    products = []  # This will contain all possible products for a given row
    for j in range(len(data[i]) - 3):
        products.append(data[i][j] * data[i][j + 1] * data[i][j + 2]
                        * data[i][j + 3])
    max_rows.append(max(products))

# print max_rows

for i in range(len(data[0])):
    products = []  # This will contain all possible products for a given column
    for j in range(len(data) - 3):
        products.append(data[j][i] * data[j + 1][i] * data[j + 2][i]
                        * data[j + 3][i])
    max_column.append(max(products))

# print max_column

for i in range(len(data) - 3):
    products = []  # This will contain all possible products for a given diagon
    for j in range(len(data[i]) - 3):
        products.append(data[i][j] * data[i + 1][j + 1] * data[i + 2][j + 2]
                        * data[i + 3][j + 3])
    max_diag_right.append(max(products))

#print max_diag_right

for i in range(len(data) - 3):
    products = []  # This will contain all possible products for a given diagon
    for j in range(3, 20):
        products.append(data[i][j] * data[i + 1][j - 1] * data[i + 2][j - 2]
                        * data[i + 3][j - 3])
    max_diag_left.append(max(products))

#print max_diag_left

print max([max(max_rows), max(max_column), max(max_diag_right),
           max(max_diag_left)])
