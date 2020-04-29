# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:42:45 2020

@author: USER
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

if __name__ == '__main__':
    head = ListNode(3)
    node1 = ListNode(0)
    node2 = ListNode(2)
    node3 = ListNode(-4)
    
    head.next = node1
    node1.next = node2
    node2.next = node3
    s = Solution()
    s.hasCycle(head)
    print("True" if s.hasCycle(l) else "False")