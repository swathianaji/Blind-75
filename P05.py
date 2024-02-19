"""
Problem: 347. Top K Frequent Elements

URL: https://leetcode.com/problems/top-k-frequent-elements/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""


def topKFrequent(nums, k):
    d ={}
    for i in nums:
        if i not in d:
            d[i] = 0
        d[i] += 1
    res = sorted(d.items(), key = lambda x: -x[1])
    return list(dict(res).keys())[:k]

# Sample test case
print(topKFrequent([1,1,1,2,2,3],2))