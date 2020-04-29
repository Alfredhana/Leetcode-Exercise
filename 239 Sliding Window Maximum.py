# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:07:26 2020

@author: USER
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deque and deque[0] <= i - k:
                deque.popleft() # outdate indices
            while deque and num > nums[deque[-1]]:
            eque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res