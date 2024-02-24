"""
Problem: 226. Invert Binary Tree

URL: https://leetcode.com/problems/invert-binary-tree/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Recursion: 
# Stopping criteria is when root becomes None
# Otherwise, swap left and right nodes after inverting them

def invertTree(self, root):
    if root is None:
        return
    temp =  root.left
    root.left = self.invertTree(root.right)
    root.right = self.invertTree(temp)
    return root
