"""
Problem: 338. Counting Bits

URL: https://leetcode.com/problems/counting-bits/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# if value is odd number which means it has 1 at the end
# if you right shift, second last digit will become last digit

def countBits(n):
    res =[]
    for i in range(n+1):
        count = 0
        while i:
            count += i%2
            i = i >> 1
        res.append(count)
    return res  

# sample test case
print(countBits(5))