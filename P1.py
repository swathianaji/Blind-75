"""
Problem: 217. Contains Duplicate

URL: https://leetcode.com/problems/contains-duplicate/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def containsDuplicate(nums) -> bool:
    d ={}
    for i in nums:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in d.values():
        if i >= 2:
            return True
    return False


# sample test case
retVal = containsDuplicate([1,2,3,1])
if retVal:
    print("Contains Duplicate")
else:
    print("Does not contain duplicate")