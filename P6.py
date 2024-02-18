"""
Problem: 238. Product of Array Except Self

URL: https://leetcode.com/problems/product-of-array-except-self/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# 1st for loop: store product of previous numbers [1,1,2,6]
# 2nd for loop: start fron the end, store product of all nums aftet current value
# reverse it [24,12,4,1]
# multiply values in both prefix and suffix list

def productExceptSelf(nums):
    prefix = [1]
    suffix = [1]
    res = []
    for i in range(1,len(nums)):
        prefix.append(nums[i-1]*prefix[-1])
    for i in range(len(nums)-2,-1,-1):
        suffix.append(nums[i+1]*suffix[-1])
    suffix = suffix[::-1]
    for i in range(len(nums)):
        res.append(prefix[i]*suffix[i])
    return res
    
# Sample test case
print(productExceptSelf([1,2,3,4]))