# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:19:13 2020

@author: USER
"""
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def maximumBinaryTree(nums):
    if nums is []:
        return None
    maxVal = -sys.maxsize
    index = 0
    for i in range(len(nums)):
        if nums[i] > maxVal:
            maxVal = nums[i]
            index = i
    root = TreeNode(maxVal)
    root.left = maximumBinaryTree(nums[0..index])
    root.right = maximumBinaryTree([index+1,len(nums)])
    return root
