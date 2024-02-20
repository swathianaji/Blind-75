"""
Problem: 190. Reverse Bits

URL: https://leetcode.com/problems/reverse-bits/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def missingNumber(nums):
    Total = 0
    for num in nums:
        Total ^= num
    rangeTotal = 0
    for i in range(len(nums)+1):
        rangeTotal ^= i
    return Total ^ rangeTotal 

# Sample test case
print(missingNumber([3,0,1]))