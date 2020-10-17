import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    blown = 0
    maximum = ar[0]
    for i in range(len(ar)):
        if(ar[i] > maximum):
            maximum = ar[i]

    for i in range(len(ar)):
        if(ar[i] == maximum):
            blown += 1
    return blown

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
