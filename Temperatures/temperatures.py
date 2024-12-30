#!/usr/bin/env python3

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

toParse = [1, -2, -8, 4, 5]
result = 0
toCheck = 0

#n = int(input())  # the number of temperatures to analyse
#for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
 #   t = int(i)
 #   toParse.append(t)

reference = abs(toParse[0])
for i in range(len(toParse) ):
    toCheck = abs(toParse[i])
    if toCheck < reference:
        reference = toCheck
    print(reference , toCheck)
print(reference)
# Write an answer using print
#print(toParse, file=sys.stderr, flush=True)
