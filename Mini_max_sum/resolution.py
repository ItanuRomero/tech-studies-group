#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minimum_sum = get_minimum_sum(arr)
    maximum_sum = get_maximum_sum(arr)
    print(f'{minimum_sum} {maximum_sum}')
    
def get_minimum_sum(integers_list):
    integers_sum = 0
    list_without_max_number = integers_list[:]
    list_without_max_number.remove(max(integers_list))
    for integer in list_without_max_number:
        integers_sum += integer
    return integers_sum
        
  
def get_maximum_sum(integers_list):
    integers_sum = 0
    list_without_min_number = integers_list[:]
    list_without_min_number.remove(min(integers_list))
    for integer in list_without_min_number:
        integers_sum += integer
    return integers_sum
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
