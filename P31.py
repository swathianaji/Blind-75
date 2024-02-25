"""
Problem: 98. Validate Binary Search Tree

URL: https://leetcode.com/problems/validate-binary-search-tree/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def inOrdertraversal(self, root,path):
    if root:
        self.inOrdertraversal(root.left, path)
        path.append(root.val)
        self.inOrdertraversal(root.right, path)

def isValidBST(self, root):
    inorder = []
    self.inOrdertraversal(root, inorder)
    return len(inorder) == len(set(inorder)) and inorder == sorted(inorder)