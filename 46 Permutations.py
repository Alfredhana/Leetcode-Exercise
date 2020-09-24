# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:30:31 2020

@author: USER
"""

def permute(nums):
    def backtrack(first=0):
        # 所有数填完
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            # 做选择
            nums[first], nums[i] = nums[i], nums[first]
            # 递归下一个数
            backtrack(first+1)
            # 撤销选择
            nums[first], nums[i] = nums[i], nums[first]
    n = len(nums)
    res = []
    backtrack()
    return res