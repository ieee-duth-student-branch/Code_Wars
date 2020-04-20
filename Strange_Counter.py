"""
Problem: https://www.hackerrank.com/challenges/strange-code/problem

References: strange-counter.py: at Algorithms>Implementation>Strange Counter
            author= "Risabh Kumar"
"""

t = int(input().strip())
rem = 3
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)
