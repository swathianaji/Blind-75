"""
Problem: 15. 3Sum

URL: https://leetcode.com/problems/3sum/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# sort the array
# a is current value, if threeSum is > 0 reduce right value, threeSum < 0 increase left value

def threeSum(nums):
    res = []
    nums = sorted(nums)

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while(l < r):
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a,nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

# Sample test case
print(threeSum([-1,0,1,2,-1,-4]))