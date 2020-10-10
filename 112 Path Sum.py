# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:29:17 2020

@author: USER
"""
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def hasPathSum(root, target):
    if root is None:
        return False
    nodes = collections.deque([root])
    vals = collections.deque([root.val])
    while nodes:
        node = nodes.popleft()
        val = vals.popleft()
        if not node.left and not node.right:
            if val == target:
                return True
                continue
        if node.left:
            nodes.append(node.left)
            vals.append(node.left.val + val)
        if node.right:
            nodes.append(node.right)
            vals.append(node.right.val + val)
def hasPathSumRecur(root, target):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return target == root.val
    return hasPathSumRecur(root.left, target - root.val) or hasPathSumRecur(root.right, target - root.val)
                
if __name__ == "__main__":
    n1 = TreeNode(4)
    n2 = TreeNode(3)
    n3 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    print(hasPathSumRecur(n1,7))