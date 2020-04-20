"""
Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?fbclid=IwAR3dt7RkrxbJVvrGD10Ze0xjlmVlYD_KLcxVmtU8NFNNMYhTtKXtt9ch3xg

References: https://github.com/sapanz/Hackerrank-Problem-Solving-Python-Solutions/blob/master/HackerRank-Breaking%20the%20Records/Breaking_the_Records.py
Author: sapanz(in github)
"""

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    maxi=scores[0]
    mini=scores[0]
    maxcount =0
    mincount=0
    for i in range(len(scores)):
        if(scores[i]>maxi):
            maxi = scores[i]
            maxcount+=1
        if(scores[i]<mini):
            mini = scores[i]
            mincount+=1
    return [maxcount, mincount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
