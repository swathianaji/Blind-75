"""
Problem: 191. Number of 1 Bits

URL: https://leetcode.com/problems/number-of-1-bits/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""
# if value is odd number which means it has 1 at the end
# if you right shift, second last digit will become last digit

def hammingWeight(n):
        count = 0
        while n:
            count += n%2
            n = n >> 1
        return count

# Sample test case
print(hammingWeight(11))