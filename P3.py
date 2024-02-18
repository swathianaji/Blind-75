"""
Problem: 1. Two Sum

URL: https://leetcode.com/problems/two-sum/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Create dictionary d, loop thru list
# If target - current element in d return indices 
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        t = target - nums[i]
        if t in d:
            return [d[t], i]
        d[nums[i]] = i
    return []

# Sample test case
print(twoSum([2,7,11,15],9))
