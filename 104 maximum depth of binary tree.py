# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:12:00 2020

@author: USER
"""
def maxDepth(root):
    if root == None:
        return 0
    else:
        return 1 + max(maxDepth(root.left),maxDepth(root.right))