# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:40:55 2020

@author: USER
"""
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
    
    
class Solution:
    def mergeTwoLists_Iteration(self, l1: ListNode, l2: ListNode) -> ListNode:
        preHead = ListNode(-1)
        prev = preHead
        
        while l1 and l2:
            if (l1.val <= l2.val):
                prev.next = l1
                print(l1.val)
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
                print(l2.val)
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return preHead.next
    
    def mergeTwoLists_Recursion(self, l1, l2):
        if l1 is None:
            print(l2.val)
            return l2
        elif l2 is None:
            print(l1.val)
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_Recursion(l1.next, l2)
            print(l1.val)
            return l1
        else:
            l2.next = self.mergeTwoLists_Recursion(l1, l2.next)
            print(l2.val)
            return l2
                

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(4)
    node2.next = node3
    node4 = ListNode(1)
    node5 = ListNode(3)
    node4.next = node5
    node6 = ListNode(4)
    node5.next = node6
    s = Solution()
    node = s.mergeTwoLists_Recursion(node1, node4)