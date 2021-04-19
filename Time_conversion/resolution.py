#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    mode = s[-2:]
    final_hour = s[2:-2]
    if mode == 'PM':
        if s[0:2] == '12':
            time = s[:-2]
        else:
            hour = s[0:2]
            hour = int(hour) + 12
            hour = str(hour)
            time = hour + final_hour
    elif mode == 'AM':
        if s[0:2] == '12':
            final_hour = s[2:-2]
            time = '00' + final_hour
        else:
            time = s[:-2]
    return time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
