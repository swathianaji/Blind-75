"""
Problem: 271. Encode and Decode Strings

URL: https://leetcode.com/problems/encode-and-decode-strings/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""
# in function encode, create new string and add length of word, one special char and word
# in decode function find the length of the word and slice it fron string and append it to result array
def encode(strs):
        """Encodes a list of strings to a single string.
        """
        s = ''
        for word in strs:
            s += str(len(word))+'#'+ word
        return s

def decode(s):
    """Decodes a single string to a list of strings.
    """
    res = []
    i = 0
    k = 0
    while(i<len(s)):
        if s[i] == "#":
            res.append(s[i+1:i+k+1])
            i += (k+1)
            k = 0
        else:
            k = k*10 + int(s[i])
            i += 1
    return res    

# Sample test case
encoded_string = encode(["Hello","World"])
print(decode(encoded_string))