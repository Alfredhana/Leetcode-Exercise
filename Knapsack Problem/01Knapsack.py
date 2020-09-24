# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:17:21 2020

@author: USER
"""

N = 4
V = 6
weight = [4, 2, 1, 5]
profit = [5, 3, 2, 8]

#f = [0] * (V+1)
#def ZeroOneKnapsack(weight, profit, i):
#    for v in range(V, weight-1, -1):
#        f[v] = max(f[v], f[v-weight]+profit)

f = [[0 * (V+1)] * (N+1)]
def ZeroOneKnapsackTwoDim(weight, profit, i):
    print(i)
    for v in range(weight, V+1):
        print(v)
        f[i][v] = f[i-1][v]
        if v >= weight[i-1]:
            f[i][v] = max(f[i][v], f[i-1][v-weight]+profit)
    
if __name__ == "__main__":
    #for i in range(0, N):
        #ZeroOneKnapsack(weight[i], profit[i], i)
    #print("Maximized Profit: %d" %f[-1])
   for i in range(0, N+1):
       ZeroOneKnapsackTwoDim(weight[i], profit[i], i)
   print("Maximized Profit: %d" %f[-1] )