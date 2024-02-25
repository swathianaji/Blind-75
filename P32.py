"""
Problem: 230. Kth Smallest Element in a BST

URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# find inorder 
# return the kth smallest from inorder list

def inOrder(self,root,path):
    if root:
        self.inOrder(root.left,path)
        path.append(root.val)
        self.inOrder(root.right,path)

def kthSmallest(self, root, k: int) -> int:
    inord = []
    self.inOrder(root,inord)
    return inord[k-1]