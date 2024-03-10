"""
Problem: 261. Graph Valid Tree

URL: https://leetcode.com/problems/graph-valid-tree/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# A tree with n nodes must contain n-1 edges
# check this and eliminate other cases
# create an adjacency list from the given edges
# perform BFS
# If the graph doesn't contain any cycles, every node must have been visited during BFS
# This means that after BFS, the length of the visited set must be equal to the number of nodes

def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if n == 1 and len(edges) == 0:
        return True

    if len(edges) != n-1:
        return False
    
    visited = set()

    hashMap = {}
    for edge in edges:
        if edge[0] not in hashMap:
            hashMap[edge[0]] = []
        if edge[1] not in hashMap:
            hashMap[edge[1]] = []
        hashMap[edge[0]].append(edge[1])
        hashMap[edge[1]].append(edge[0])

    if 0 not in hashMap:
        return False

    queue = deque([0])

    while queue:
        currNode = queue.popleft()
        visited.add(currNode)
        for node in hashMap[currNode]:
            if node not in visited:
                queue.append(node)
    
    return len(visited) == n