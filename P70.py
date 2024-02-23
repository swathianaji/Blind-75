"""
Problem: 73. Set Matrix Zeroes

URL: https://leetcode.com/problems/set-matrix-zeroes/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# store the position of zeros in to row and col lists
# traverse thru matrix and change to zeros

def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    for i in range(len(row)):
        for j in range(len(matrix[0])):
            matrix[row[i]][j] = 0

    for i in range(len(matrix)):
        for j in range(len(col)):
            matrix[i][col[j]] = 0
