# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:42:08 2020

@author: USER
"""
import queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mindepth(head):
    if head == None: return 0
    q = queue.Queue()
    q.put(head)
    depth = 1
    while not q.empty():
        for i in range(q.qsize()):
            cur = q.get()
            if cur.left == None and cur.right == None:
                return depth
            if cur.left != None:
                q.put(cur.left)
            if cur.right != None:
                q.put(cur.right)
        depth += 1
    return depth
    
    
if __name__ == '__main__':
    head = TreeNode(3)
    leaf1 = TreeNode(9)
    leaf2 = TreeNode(20)
    leaf3 = TreeNode(15)
    leaf4 = TreeNode(7)
    
    head.left = leaf1
    head.right = leaf2
    leaf2.left = leaf3
    leaf2.right = leaf4
    
    print(mindepth(head))