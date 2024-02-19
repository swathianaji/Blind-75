"""
Problem: 3. Longest Substring Without Repeating Characters

URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# let's use two pointers, r will be keep moving
# l will move only when there is duplicates in substring
# keep track of highest substring len


def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    r = 1
    length = 1
    if len(s) <=1:
        return len(s)
    while(r <= len(s)):
        subString = s[l:r]
        if len(subString) == len(set(subString)):
            length = max(length, len(subString))
            r += 1
        else:
            l += 1
    return length
            
# Sample test case
print(lengthOfLongestSubstring("abcabcbb"))