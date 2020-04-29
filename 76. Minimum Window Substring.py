# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:09:50 2020

@author: USER
"""
from collections import Counter

def minWindow(s, t):
    min_len = len(s) + 1
    start, left, right = 0, 0, 0
    window = {}
    needs = {}
    for c in t:
        needs[c] = needs.get(c,0)+1
    match = 0
    while right < len(s):
        c1 = s[right]
        if c1 in needs:
            window[c1] = window.get(c,0)+1
            if window[c1] == needs[c1]:
                match += 1
        right += 1
        while match == len(needs):
            if (right - left < min_len):
                start = left
                print(start)
                min_len = right - left
            c2 = s[left]
            if c2 in needs:
                window[c2] -= 1
                if window[c2] < needs[c2]:
                    match -= 1
            left += 1
    if min_len == len(s) + 1:
        return ""
    else:
        return s[start:start+min_len]
    
if __name__ == '__main__':
    print(minWindow('adobecodebanc','abc'))
       
    
        