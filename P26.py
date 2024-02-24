"""
Problem: 104. Maximum Depth of Binary Tree

URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""


# Stopping criteria: when there is no node, we can say that max depth is 0
# Otherwise, take the max depth from both left and right subtrees, and add 1 to it (this is to count the current node)
def maxDepth(self, root):
    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))