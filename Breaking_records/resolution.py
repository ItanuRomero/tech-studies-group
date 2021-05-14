#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    return_list = list()
    record_high = record_low = breake_record = bad_record = 0
    
    for point in scores:
        if point > record_high:
            if record_high != 0:
                breake_record += 1
            record_high = point
        if point < record_low or record_low == 0:
            if record_low != 0:
                bad_record += 1
            record_low = point
    
    return_list.append(breake_record)
    return_list.append(bad_record)
    return return_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
