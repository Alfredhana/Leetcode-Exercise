# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:31:33 2020

@author: USER
"""
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def __init__(self):
        self.pre = -sys.maxsize
    def isValidBST(self,root):
        if root == None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
    
class Solution2(object):
    def __init__(self):
        self.res = []
    def isValidBST(self,root):
        if root == None:
            return True
        self.inorder(root)
        for i in range(1, len(self.res)):
            if self.res[i-1] >= self.res[i]:
                return False
        return True
        
    def inorder(self,root):
        if not root is None:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)

if __name__ == "__main__":
    n1 = TreeNode(4)
    n2 = TreeNode(3)
    n3 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    s = Solution()
    print(s.isValidBST(n1))