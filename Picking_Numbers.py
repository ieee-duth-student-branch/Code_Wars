"""
Problem: Picking Numbers (https://www.hackerrank.com/challenges/picking-numbers/problem)

"""

freq = [0 for i in range(101)]
    max_pair = 0
    for n in a:
        freq[n] += 1
        max_pair = max(max_pair, max((freq[n] + freq[n-1]), (freq[n] + freq[n+1])))
    return max_pair
