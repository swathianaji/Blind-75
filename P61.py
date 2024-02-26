"""
Problem: 53. Maximum Subarray

URL: https://leetcode.com/problems/maximum-subarray/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""


# Kadane's Algorithm

def maxSubArray(nums):
    maxSofar = float('-inf')
    maxEndinghere = 0
    for i in range(len(nums)):
        maxEndinghere +=nums[i]
        maxSofar = max(maxSofar, maxEndinghere)
        if maxEndinghere < 0:
            maxEndinghere = 0
    return maxSofar  

# Sample test cases
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))