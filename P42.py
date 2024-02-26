"""
Problem: 200. Number of Islands

URL: https://leetcode.com/problems/number-of-islands/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows = len(grid) 
    cols = len(grid[0])
    visited = set()
    island = 0

    def BFS(r,c):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row,col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                r,c = row+dr, col+dc
                if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                BFS(r,c)
                island += 1
    return island