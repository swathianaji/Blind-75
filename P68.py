"""
Problem: 48. Rotate Image

URL: https://leetcode.com/problems/rotate-image/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Transpose matrix and reverse it 

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]