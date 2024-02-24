"""
Problem: 235. Lowest Common Ancestor of a Binary Search Tree

URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# If both p and q are less than root node traverse left.
# if both p and q are greater than root node traverse right.
# in any other case, root will be (root.val >= p.val and root.val  <= q.val) or (root.val >= q.val and root.val  <= p.val)

def lowestCommonAncestor(self, root, p, q) :
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root