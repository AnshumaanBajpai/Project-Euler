# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 13:51:49 2014

@author: Anshumaan
"""

## This code takes the large 1000 digit number from problem 8 as a string input ## and then splits it into multiple strings at 0s. It then figures out how many ## of those strings are 13 or larger in length. It then calculates the  required## product and compares.

a_1 = "73167176531330624919225119674426574742355349194934"
a_2 = "96983520312774506326239578318016984801869478851843"
a_3 = "85861560789112949495459501737958331952853208805511"
a_4 = "12540698747158523863050715693290963295227443043557"
a_5 = "66896648950445244523161731856403098711121722383113"
a_6 = "62229893423380308135336276614282806444486645238749"
a_7 = "30358907296290491560440772390713810515859307960866"
a_8 = "70172427121883998797908792274921901699720888093776"
a_9 = "65727333001053367881220235421809751254540594752243"
a_10 = "52584907711670556013604839586446706324415722155397"
a_11 = "53697817977846174064955149290862569321978468622482"
a_12 = "83972241375657056057490261407972968652414535100474"
a_13 = "82166370484403199890008895243450658541227588666881"
a_14 = "16427171479924442928230863465674813919123162824586"
a_15 = "17866458359124566529476545682848912883142607690042"
a_16 = "24219022671055626321111109370544217506941658960408"
a_17 = "07198403850962455444362981230987879927244284909188"
a_18 = "84580156166097919133875499200524063689912560717606"
a_19 = "05886116467109405077541002256983155200055935729725"
a_20 = "71636269561882670428252483600823257530420752963450"

a = (a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7 + a_8 + a_9 + a_10 + a_11 + a_12
     + a_13 + a_14 + a_15 + a_16 + a_17 + a_18 + a_19 + a_20)


## We now split the entire string into various strings with 0 as the seperator
## because any string with zero in it will have 0 as the product. We then take
## only the strings that are more than 13 in length.


split_zero = a.split("0")
split_zero_13 = [i for i in split_zero if len(i) > 12]


products = []  # initialize a list to hold the max product from each string

for i in range(len(split_zero_13)):
    product_temp = []  # initialize a list for products from each string
    for j in range(len(split_zero_13[i]) - 12):
        product_temp.append(reduce(lambda x, y: x * y,
                                   [int(split_zero_13[i][j:j + 13][k])
                                       for k in range(13)]))
    products.append(max(product_temp))


## We can also have just one variable that store only the most recent product
## and updates the value only if the new product is larger than the exisiting
## value of the product variable.


print max(products)
