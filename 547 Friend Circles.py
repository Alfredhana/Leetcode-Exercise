# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:31:02 2020

@author: USER
"""
class solution:
    def find(self, parent, i):
        if (parent[i] == -1):
            return i;
        return self.find(parent, parent[i])
    def union(self, parent, p, q):
        pID = self.find(parent, p)
        qID = self.find(parent, q)
        if (pID != qID):
            parent[pID] = qID
    def findCircleNum(self, m):
        parent = [-1] * len(m)
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] == 1 and i != j:
                    self.union(parent, i, j)
        count = 1
        for i in range(len(parent)):
            count += 1
        return count
print(solution().findCircleNum([[1,1,0], [1,1,0], [0,0,1]]))