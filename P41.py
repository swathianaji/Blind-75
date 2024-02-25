"""
Problem: 39. Combination Sum

URL: https://leetcode.com/problems/combination-sum/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        def DFS(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            curr.append(candidates[i])
            DFS(i,curr,total+candidates[i])
            curr.pop()
            DFS(i+1,curr,total)
        
        DFS(0,[],0)
        return res