"""
Problem: 100. Same Tree

URL: https://leetcode.com/problems/same-tree/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""



def isSameTree(self, p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))