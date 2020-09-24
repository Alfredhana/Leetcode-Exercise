# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:45:20 2020

@author: USER
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre