# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:56:10 2020

@author: USER
"""


class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapNodes(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next