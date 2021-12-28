#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(
    starting_point, 
    ending_point, 
    apple_tree, 
    orange_tree, 
    apples, 
    oranges
    ):
    sams_house = {
        'start': starting_point, 
        'end':ending_point
    }
    apples_on_sams_house = count_fruits(sams_house, apple_tree, apples)
    oranges_on_sams_house = count_fruits(sams_house, orange_tree, oranges)
    print(f'{apples_on_sams_house}\n{oranges_on_sams_house}')
    

def count_fruits(sams_house, tree, fruits):
    how_many = 0
    for fruit in fruits:
        position = tree + fruit 
        if sams_house['start'] <= position <= sams_house['end']:
            how_many += 1
    return how_many

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
