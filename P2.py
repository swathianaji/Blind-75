"""
Problem: 242. Valid Anagram

URL: https://leetcode.com/problems/valid-anagram/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Create dictionary d and count each letter
# In second for loop subtract count using t string
# Return true if sum of dictionary values is equal to 0 and len of set of d.values equal to 1
def isAnagram(s,t) -> bool:
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    for i in range(len(t)):
        if t[i] in d:
            d[t[i]] -= 1
        else:
            return False
    return sum(d.values()) == 0 and len(set(d.values())) == 1

# Sample test case
print(isAnagram( "anagram", "nagaram"))