# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:06:36 2020

@author: USER
"""

class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.right)
        dfs(root)
        return self.res