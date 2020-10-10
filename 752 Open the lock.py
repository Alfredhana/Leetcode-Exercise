# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:20:33 2020

@author: USER
"""
def plusOne(s, j):
    ls = list(s)
    if ls[j] == '9':
        ls[j] = '0'
    else:
        ls[j] = str(int(ls[j]) + 1)
    return "".join(ls)

def minusOne(s, j):
    ls = list(s)
    if ls[j] == '0':
        ls[j] = '9'
    else:
        ls[j] = str(int(ls[j]) - 1)
    return "".join(ls)

def openLock(deadends, target):
    q = set()
    q.add("0000")
    
    visited = set()
    visited.add("0000")
    
    deads = set()
    for end in deadends:
        deads.add(end)
    step = 0
    while q:
        for i in range(len(q)):
            cur = q.pop()
            print(cur)
            if cur in deads:
                continue
            if cur == target:
                return step
            for j in range(4):
                up = plusOne(cur, j)
                if up not in visited:
                    q.add(up)
                    visited.add(up)
                
                down = minusOne(cur, j)
                if down not in visited:
                    q.add(down)
                    visited.add(down)
        step += 1
    return -1
    
if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(openLock(deadends, target))