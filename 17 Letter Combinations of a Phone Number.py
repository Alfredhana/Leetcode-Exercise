# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:44:46 2020

@author: USER
"""

class Solution:
    def lettercombinations(self, digits):
        print(digits)
        phoneMap = {'2':['a', 'b', 'c'],
                 '3':['d', 'e', 'f'],
                 '4':['g', 'h', 'i'],
                 '5':['j', 'k', 'l'],
                 '6':['m', 'n', 'o'],
                 '7':['p', 'q', 'r', 's'],
                 '8':['t', 'u', 'v'],
                 '9':['w', 'x', 'y', 'z']}
        def findcombination(digits, combination):
            if len(digits) == 0:
                list.append(combination)
            else:
                for letter in phoneMap[digits[0]]:
                    findcombination(digits[1:], combination + letter)
        list = []
        if digits:
            findcombination(digits, "")
        print( list)
        
        
if __name__ == '__main__':
    s = Solution()
    letters = "79"
    print(letters)
    s.lettercombinations(letters);