#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
PROGRAMMER_DAY = 256
CALENDAR_DAYS_BY_TYPE = {
    'julian': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    'gregorian': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    'transition': [31, 15, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
}


def dayOfProgrammer(year):
    calendar_type = get_calendar_type(year)
    day, month = get_programmer_day_and_month(calendar_type, year)
    
    return formatted_output(day, month, year)

    
def get_calendar_type(year):
    if year < 1918:
        return 'julian'
    elif year > 1918:
        return 'gregorian'
    else:
        return 'transition'

      
def get_programmer_day_and_month(calendar_type, year):
    calendar_months = CALENDAR_DAYS_BY_TYPE[calendar_type]
    month, total = get_programmer_month(calendar_months)
    print(total)
    day = PROGRAMMER_DAY - total
    if is_leap_year(calendar_type, year):
        day -= 1
    return [day, month]

    
def get_programmer_month(calendar_months):
    total = month = 0
    while total < PROGRAMMER_DAY:
        total += calendar_months[month]
        month += 1
    sum_days = total - calendar_months[month - 1]
    return month, sum_days

    
def is_leap_year(calendar_type, year):
    if calendar_type == 'julian':
        if year % 4 == 0:
            return True
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        return False

    
def formatted_output(day, month, year):
    return f'{day}.{month:02}.{year}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
