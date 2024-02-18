"""
Problem: 125. Valid Palindrome

URL: https://leetcode.com/problems/valid-palindrome/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""
# initialize new string, loop thru each letter, add lower case letter if isalnum().
# Traverse from both ends and compare each letter, return False if mismatch found.
def isPalindrome(s) :
    word =''
    for i in s:
        if i.isalnum():
            word += i.lower()
    i = 0
    j = len(word)-1
    while(i<j):
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

#sample test case
print(isPalindrome("A man, a plan, a canal: Panama"))