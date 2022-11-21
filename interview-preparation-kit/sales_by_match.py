#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # 1 - Extract pairs
    # 2 - Increment pair counter
    pair_counter = 0
    # memoized colors to prevent already done computation
    examined_colors = [] 
    for i in range(n):
        color = ar[i]
        if color not in examined_colors:
            examined_colors.append(color)
            color_pairs = [color]
            for j in range(i+1, n):
                curr_color = ar[j]
                if curr_color == color:
                    color_pairs.append(curr_color)
            print(color_pairs)
            pair_counter += math.floor(len(color_pairs) / 2)
    return pair_counter


if __name__ == '__main__':
    ar = list(map(int, "10 20 20 10 10 30 50 10 20".rstrip().split()))
    result = sockMerchant(len(ar), ar)
    print(result)
