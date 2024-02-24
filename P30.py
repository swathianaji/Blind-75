"""
Problem: 102. Binary Tree Level Order Traversal

URL: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Breadth first search
# If there is no root, do nothing and return
# Take a queue with root node
# at every step, traverse through the entirety of the queue (at every step, queue contains one level of the tree)
# pop one node at a time, append its value to the result, and push left child and right child to the queue.

def levelOrder(self, root):
    res = []
    q = deque([root])
    if not root:
        return None
    while q:
        l = []
        for i in range(len(q)):
            node = q.popleft()
            l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(l)
    return res