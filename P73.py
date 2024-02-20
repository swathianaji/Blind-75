"""
Problem: 190. Reverse Bits

URL: https://leetcode.com/problems/reverse-bits/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def reverseBits(self, n: int) -> int:
    res = []
    reverse = 0
    while n:
        res.append(n%2)
        n = n >> 1
    res += [0] * (32-len(res))
    for i in res:
        reverse = reverse * 2 + i  #convert bin to integer
    return reverse

