"""
Problem: 79. Word Search

URL: https://leetcode.com/problems/word-search/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        path = set()

        def DFS(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols
            or word[i] != board[r][c] or (r,c) in path):
                return False

            path.add((r,c))
            res = ( DFS(r+1,c,i+1) or
                    DFS(r-1,c,i+1) or
                    DFS(r,c+1,i+1) or
                    DFS(r,c-1,i+1))
            path.remove((r,c))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if DFS(i,j,0): return True
        return False
            
        