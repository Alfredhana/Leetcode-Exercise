# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:36:46 2020

@author: USER
"""
import sys
import random

def Rand5():
    return random.randint(1,5)

def Rand7():
    n = sys.maxsize
    while n > 21:
        n = (Rand5() - 1) * 5 + Rand5()
    return (n - 1) % 7 + 1

        

if __name__ == '__main__':
    print(Rand7())