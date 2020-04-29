# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:13:07 2020

@author: USER
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         

def reverse(node):
    pre =  ListNode(0)
    cur = nxt = node
    while cur != None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre.val
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    
    print(reverse(n1))