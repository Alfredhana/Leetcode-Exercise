# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 00:34:04 2020

@author: USER
"""

def hasCycle(head):
    fast = slow = head;
    while fast!=null and fast.next!=null:
        fast = fast.next.next
        slow = slow.next
        if fast == slow 
    		break
    while fast!=null and fast.next!=null:
    	fast = fast.next.next
    	slow = slow.next
	return slow