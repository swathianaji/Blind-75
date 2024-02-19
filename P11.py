"""
Problem: 11. Container With Most Water

URL: https://leetcode.com/problems/container-with-most-water/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# use left and right pointer
# find area using minimum of two pointer and length
# shift pointer which is less

def maxArea(height):
    l = 0
    r = len(height)-1
    mx = 0
    while(l < r):
        area = min(height[l], height[r])*(r-l)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
        mx = max(mx, area)
    return mx

# Sample test case
print(maxArea([1,8,6,2,5,4,8,3,7]))