#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    quantity_of_elements = get_quantity_of_elements(arr)
    positive_ratio, negative_ratio, zero_ratio = get_ratios(quantity_of_elements, len(arr))
    print(f'{positive_ratio:.6f}')
    print(f'{negative_ratio:.6f}')
    print(f'{zero_ratio:.6f}')


def get_quantity_of_elements(elements):
    positive_elements = [element for element in elements if element > 0]
    negative_elements = [element for element in elements if element < 0]
    null_elements = [element for element in elements if element == 0]
    positive_count, negative_count, null_count = \
        len(positive_elements), len(negative_elements), len(null_elements)
    return [positive_count, negative_count, null_count]

    
def get_ratios(quantity_of_elements, total_length):
    ratios = [element_quantity / total_length for element_quantity in quantity_of_elements]
    return ratios
        
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
