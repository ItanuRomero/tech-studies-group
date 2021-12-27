#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(alice_triplet, bob_triplet):
    bob_points = alice_points = 0
    for element in range(0, 3):
        if alice_triplet[element] > bob_triplet[element]:
            alice_points += 1
        elif bob_triplet[element] > alice_triplet[element]:
            bob_points += 1
    return [alice_points, bob_points]          
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
