# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:51:28 2020

@author: USER
"""
import queue

class Node(object):
    def __init__(self, x):
        self.val = x
        self.neighbors = []
    def neighbor(self,n):
        self.neighbors.append(n)
    def adj(self):
        return self.neighbors

def BFS(start, target):
    q = queue.Queue()
    visited = []
    q.put(start)
    visited.append(start)
    step = 0
    while not q.empty():
        for i in range(q.qsize()):
            cur = q.get()
            if cur is target:
                return step
            for x in cur.adj():
                if x not in visited:
                    q.put(x)
                    visited.append(x)
        step += 1

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    
    n1.neighbor(n2)
    n1.neighbor(n3)
    n3.neighbor(n4)
    n4.neighbor(n5)
    n4.neighbor(n6)
    n4.neighbor(n7)
    n6.neighbor(n7)
    print(BFS(n1,n7))