"""
Problem: 70. Climbing Stairs

URL: https://leetcode.com/problems/climbing-stairs/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def climbStairs(self, n: int) -> int:
    arr = [0, 1, 2]
    for i in range(3, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]