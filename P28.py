"""
Problem: 572. Subtree of Another Tree

URL: https://leetcode.com/problems/subtree-of-another-tree/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# isSame
# Stopping criteria:
#   - True case : if both p and q become none
#   - False case: if one of them is none, or values are different
# Otherwise, (if both vals are same), check if left subtrees are same, and right subtrees are same.

# isSubtree
# there will be subroot, so check if root not exist 
# when there is match with subtree, call isSame function

def isSame(self,p,q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return (self.isSame(p.left,q.left) and self.isSame(p.right,q.right))

def isSubtree(self, root, subRoot):
    if not root:
        return False
    if root.val == subRoot.val:
        if self.isSame(root,subRoot):
            return True
    return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)