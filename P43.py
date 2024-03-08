"""
Problem: 133. Clone Graph

URL: https://leetcode.com/problems/clone-graph/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Use hashmap to to keep track of copy
# if Node is not in dictionary make a copy and add it
# call dfs on node neighbors 
        
def cloneGraph(self, node):
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    
    return dfs(node) if node else None