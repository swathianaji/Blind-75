"""
Problem: 153. Find Minimum in Rotated Sorted Array

URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Consider 1 element as target value to compare
# if target value is less than mid, minimum is in left half
# if target value is greater than mid, minimum is in right half

def findMin(nums):
    l = 1
    r = len(nums)-1
    while(l<=r):
        mid = (l+r)//2
        if nums[0] < nums[mid]:
            l = mid + 1
        elif nums[0] > nums[mid]:
            r = mid -1
    if l >= len(nums):
        return nums[0]
    return nums[l]   

# Sample test case
print(findMin([3,4,5,1,2]))