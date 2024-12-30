#!/usr/bin/env python3

import sys
import math

toParse = []
toCheck = []
finalResult = 0
j = 0
i = 0

n = int(input())
for i in input().split():
    v = int(i)
    toParse.append(v)
print(toParse, file=sys.stderr, flush=True)
print(len(toCheck), file=sys.stderr, flush=True)

reference = toParse[0]
for i in range(len(toParse) -1):
    if toParse[i] > toParse[i+1]:
        while toParse[i] > toParse[i+1]:
            if len(toCheck) < j:
                toCheck.append(0)
            toCheck[j] = toCheck[j] + (-(abs(toParse[i]) - abs(toParse[i+1])))
            i+=1
        j+=1


toCheck.sort()
if toCheck == [] or toCheck[0] > 0:
    print("0")
else:
    print(toCheck[0])

# To debug: 
print(toCheck, file=sys.stderr, flush=True)
