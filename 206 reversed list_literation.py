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
        pre = None
		cur = head
		while cur:
			tmp = cur.next
			cur.next = pre
			pre = cur
			cur = tmp
		return pre	