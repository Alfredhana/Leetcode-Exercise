# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:01:05 2020

@author: USER
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def invertTree(root):
    if root == None:
        return None
    invertTree(root.left)
    invertTree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp