# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def __init__(self):
        self.l = []
    def preorderTraversal(self, root):
        if root == None:
            return []
        self.preorderTraversal(root.left)
        self.l.append(root.val)
        self.preorderTraversal(root.right)
        return self.l
    
    def preorderTraversal_stack(self, root):
        if root == None:
            return []
        cur = root
        mystack = []
        outstack = []
        while mystack or cur:
            while cur:
                mystack.append(cur)
                cur  = cur.left
            tmp = mystack.pop()
        
        return self.l

if __name__ == '__main__':
    r1 = TreeNode(1)
    r2 = TreeNode(7)
    r3 = TreeNode(3)
    r4 = TreeNode(4)
    r5 = TreeNode(5)
    
    r1.left = r3
    r1.right = r2
    r3.left = r4
    r4.left = r5
    
    s = Solution()
    print(s.preorderTraversal(r1))