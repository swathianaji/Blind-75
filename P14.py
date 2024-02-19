"""
Problem: 424. Longest Repeating Character Replacement

URL: https://leetcode.com/problems/longest-repeating-character-replacement/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# using two pointer, r will be moving ahead for every iteration
# add values to dictionary as r in for loop moves
# maintain max frequecy of the window, jus after updating dictionary 
# if window length - maxf crosses operations that can be performed(k), start moving left 
# store max len of substring in res  

def characterReplacement(s, k):
    l = 0
    maxf = 0
    res = 0
    d = {}
    for r in range(len(s)):
        if s[r] not in d:
            d[s[r]] = 0
        d[s[r]] += 1
        maxf = max(maxf,d[s[r]]) 
        while r-l+1 - maxf > k:
            d[s[l]] -= 1
            l += 1
        res = max(res, r-l+1)   
    return res

# Sample test case
print(characterReplacement("AABABBA",1))