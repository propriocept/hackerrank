#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    # Calculate the differences once.
    diffs = [
        pump[0] - pump[1] for pump in petrolpumps
    ]
    # Don't calculate all possible routes. Can only start if the amount
    # of petrol >= distance to next station.
    possible_starts = [i for i, tank in enumerate(diffs) if tank > 0]
    if len(possible_starts) == 1:
        return possible_starts[0]
    
    # If there is more than one solution, start grinding.
    for start in possible_starts:
        tank: int = 0
        for x in range(n):
            tank += diffs[(start + x)%n]
            if tank < 0:
                break  # stop as soon as possible
        if x == n - 1:
            return start  # once we have a solution, stop

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
