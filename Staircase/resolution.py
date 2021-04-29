#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    stairs_volumn = ''
    staircase_str = ''
    for times in range(1, n + 1):
        for stair in range(1, times + 1):
            stairs_volumn += '#'
        staircase_str += "{:>{}}".format(stairs_volumn, n)
        staircase_str += '\n'
        stairs_volumn = ''
    print(staircase_str)
    return staircase_str
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
