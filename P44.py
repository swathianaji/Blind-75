"""
Problem: 417. Pacific Atlantic Water Flow

URL: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Write DFS to check if position reaches ocean by checking if values from edge to position are inceasing in order
# Create two sets of two oceans
# In first for loop to run dfs on top and bottom rows and add positions to respective sets
# In second for loop to run dfs on left and right cols and add positions to respective sets
# Finally, go thru every position in matrix and if position is in both the sets add it to result

def pacificAtlantic(self, heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac , alt = set(), set()

    def dfs(r,c,visit,prevHeight):
        if((r,c) in visit or r < 0 or c < 0 or r ==  ROWS or c == COLS or heights[r][c] < prevHeight):
            return
        visit.add((r,c))
        dfs(r+1, c, visit, heights[r][c])
        dfs(r-1, c, visit, heights[r][c])
        dfs(r, c+1, visit, heights[r][c])
        dfs(r, c-1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS-1, c, alt, heights[ROWS-1][c])
    
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r,COLS-1, alt, heights[r][COLS-1])

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in pac and (r,c) in alt:
                res.append([r,c])
    return res

