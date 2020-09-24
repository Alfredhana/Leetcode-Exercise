# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 00:35:21 2020

@author: USER
"""

def hasCycle(head, k) 
	slow = fast = head
	while k > 0:
        k -= 1
    	fast = fast.next

    // 上面的代码类似 hasCycle 函数
    slow = head
    while (slow != fast):
        fast = fast.next
        slow = slow.next
    return slow