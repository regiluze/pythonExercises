#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colorMatch = {}
    for color in ar:
        num = colorMatch.get(color, 0) + 1
        colorMatch[color] = num
    pairs = sum(list(map(lambda x: x // 2, list(colorMatch.values()))))
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

