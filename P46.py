"""
Problem: 323. Number of Connected Components in an Undirected Graph

URL: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Number of connected components is the number of times queue becomes empty during BFS
# Firstly, we'll construct an adjacency list from the given edges (list of lists)
# Maintain a bool array named visited to keep track of the nodes that are explored
# The goal is to visit every node in the graph, and count connected components when BFS queue becomes empty
# We will continue our loop until there are no unvisited nodes
# Find the first node that is not explored, and then start BFS from the node.
# When this BFS ends, increment the number of connected components counter

def countComponents(self, n: int, edges: List[List[int]]) -> int:
    visited = [False for i in range(n)]
    numComp = 0
    edgeMap = {}

    for edge in edges:
        if edge[0] not in edgeMap:
            edgeMap[edge[0]] = []
        if edge[1] not in edgeMap:
            edgeMap[edge[1]] = []
        edgeMap[edge[0]].append(edge[1])
        edgeMap[edge[1]].append(edge[0])

    while visited.count(False) != 0:
        node = visited.index(False)
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            visited[currNode] = True
            if currNode in edgeMap:
                for node in edgeMap[currNode]:
                    if not visited[node]:
                        queue.append(node)
        numComp += 1

    return numComp