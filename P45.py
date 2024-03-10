"""
Problem: 207. Course Schedule

URL: https://leetcode.com/problems/course-schedule/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    preMap = {i:[] for i in range(numCourses)}
    for crs,pre in prerequisites:
        preMap[crs].append(pre)

    visitedSet = set()
    def dfs(crs):
        if preMap[crs] == []:
            return True
        if crs in visitedSet:
            return False
        visitedSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        visitedSet.remove(crs)
        preMap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs): return False
    return True