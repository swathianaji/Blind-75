"""
Problem: 49. Group Anagrams

URL: https://leetcode.com/problems/group-anagrams/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# loop thru words in strs, sort by making word as list as sorted workd only for iterables.
# create list and append words that are similar to sorted word
# return dictionary values

def groupAnagrams(strs):
    d = {}
    for i in strs:
        word = ''.join(sorted(list(i)))
        if word not in d:
            d[word] = []
        d[word].append(i)
    return list(d.values())

# Sample test case
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))