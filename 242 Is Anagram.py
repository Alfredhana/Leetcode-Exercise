# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 00:40:48 2020

@author: USER
"""

def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    counter = [0 for i in range(26)]
    for i in range(len(s)):
        counter[ord(s[i]) - ord('a')] += 1
        counter[ord(t[i]) - ord('a')] -= 1
    for count in counter:
        if count != 0:
            return False