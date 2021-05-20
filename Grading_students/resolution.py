#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grades = list()
    teorical_grade = 0
    for grade in grades:
        if grade < 40:
            if grade >= 38:
                grade = 40
        else:
            teorical_grade = grade
            for i in range(0, 2):
                teorical_grade += 1
                if teorical_grade % 5 == 0:
                    grade = teorical_grade
                    break
        final_grades.append(grade)
    return final_grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
