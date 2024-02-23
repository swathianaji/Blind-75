"""
Problem: 54. Spiral Matrix

URL: https://leetcode.com/problems/spiral-matrix/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Initially, we take four variables for each row, col, start and end pair
# one variable to fix the direction in the current iteration
# In each iteration, we add values from colStart to colEnd, and then from rowStart to rowEnd, to the result
# Update all four variables based on the conditions in the image
# The direction is flipped in every iteration
# Stopping criteria: when rowStart == rowEnd, or colStart == colEnd
def spiralOrder(matrix):
    rowStart = 0
    colStart = 0
    rowEnd = len(matrix) - 1
    colEnd = len(matrix[0]) - 1
    direction = 1
    res = []
    while True:
        i = rowStart
        for j in range(colStart,colEnd+direction,direction):
            res.append(matrix[i][j])
        
        j = colEnd
        for i in range(rowStart+direction,rowEnd+direction,direction):
            res.append(matrix[i][j])
                
        if (rowStart == rowEnd) or (colStart == colEnd):
            break

        # row variables updation
        temp = rowStart
        rowStart = rowEnd
        rowEnd = temp + direction

        #col variables updation
        temp = colStart
        colStart = colEnd - direction
        colEnd = temp

        direction *= -1

    return res