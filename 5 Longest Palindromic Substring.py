# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:38:35 2020

@author: USER
"""

def palindrome(s, l, r):
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1
    return s[l+1:r-l-1]

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        s1 = palindrome(s, i, i)
        s2 = palindrome(s, i ,i + 1)
        if len(res) <= len(s1):
            res = s1
        if len(res) <= len(s2):
            res = s2
    return res

if __name__ == '__main__':
    print(longestPalindrome("babab"))