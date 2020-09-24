# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:20:53 2020

@author: USER
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
         
sep = ","
null = "#"
sb = []

def traverse(root, sb):
    if root == None:
        sb.append(null).append(sep)
        return
    sb.append(root.val).append(sep)
    traverse(root.left, sb)
    traverse(root.right, sb)
    
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    
    print(reverse(n1))