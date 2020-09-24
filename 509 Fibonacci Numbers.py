# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 00:23:59 2020

@author: USER
"""

def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n-1) + fib(n-2)

def fibMemo(n):
    if n < 1: return 0
    memo = [0] * (n+1)
    return helper(memo, n)

def helper(memo, n):
    if n == 1 or n == 2: return 1
    if memo[n] != 0: return memo[n]
    memo[n] = helper(memo, n-1) + helper(memo, n-2)
    return memo[n]

def fibDP(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]