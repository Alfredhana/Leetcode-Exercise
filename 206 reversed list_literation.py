# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:45:20 2020

@author: USER
"""

 Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        cur = ListNode(None)
        pre = head
        while pre != None:
            t = pre.next
            pre.next = cur0
            cur = pre
            pre = t
        return cur