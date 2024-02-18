"""
Problem: 128. Longest Consecutive Sequence

URL: https://leetcode.com/problems/longest-consecutive-sequence/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# add count to dictionary
# starting number to count, if k-1 is not in dictionary 
# count from k+1 using i and get length by subtracting k from i


def longestConsecutive(nums):
    d ={}
    mx = 0
    for i in nums:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for k,v in d.items():
        if k-1 not in d:
            i = k+1
            while i in d:
                i += 1
            mx = max(mx,i-k)
    return mx

# Sample test case
print(longestConsecutive([100,4,200,1,3,2]))