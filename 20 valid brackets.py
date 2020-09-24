# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:21:10 2020

@author: USER
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {')':'(',']':'[','}':'{'}
        for c in s:
            if c not in dict:
                stack.append(c)
            elif not stack or dict[c] != stack.pop():
                return False
        return not stack
    

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("({()})"))