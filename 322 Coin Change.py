# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:22:44 2020

@author: USER
"""
def coinChange(coins, amount):
    dp = [amount+1]*(amount+1)
    dp[0]=0
    for i in range(len(dp)):
        for coin in coins:
            if (i-coin<0):
                continue
            dp[i]=min(dp[i],1+dp[i-coin])

    return -1 if dp[amount] == amount + 1 else dp[amount]