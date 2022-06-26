#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    # 4x4 (n=2)
    # abba
    # cddc
    # cddc
    # abba
    ###
    # 6x6 (n=3)
    # abccba
    # deffed
    # ghiihg
    # ghiihg
    # deffed
    # abccba
    ###
    # 8x8 (n=4)
    # abcddcba
    # efghhgfe
    # ijkllkji
    # mnoppomn
    # ...
    ### 6x6 (n=3)
    # a: 0, 0; 0, 2n-1; 2n-1, 0; 2n-1, 2n-1
    # b: 0, 1; 0, 2n-1-1; 2n-1-1, 1; 2n-1, 2n-1-1
    # c: 0, 2; 0, 2n-1-1-1; 2n-1-1-1, 2; 2n-1-1-1, 2n-1-1-1
    # d: 1, 0; 1, 2n-1; 2n-1-1, 0; 2n-1-1, 2n-1-1
    
    tot = 0
    for row in range(n):
        for col in range(n):
            tot += max(
                matrix[row][col],
                matrix[row][2*n - 1 -col],
                matrix[2*n -1 -row][col],
                matrix[2*n -1 -row][2*n -1 -col],
            )
    return tot
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
