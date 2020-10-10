# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:10:20 2020

@author: USER
"""

def trailingZeroes(n):
    res = 0
    divisor = 5
    while divisor <= n:
        res += n / divisor
        divisor *= 5
    return res