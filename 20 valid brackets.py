# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:21:10 2020

@author: USER
"""

class Solution(object):
    def isValid(self, s):
        if s == None:
            return
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False 
        return len(stack) == 1