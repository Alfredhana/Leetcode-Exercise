# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:55:31 2020

@author: USER
"""

def countPrimes(n):
    count = 0
    for i in range(2, n):
        if (isPrime(i)):
            count += 1
    return count

def isPrime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def countPrimes_v2(n):
    isPrim = [True] * n
    for i in range(2, n):
        if isPrim[i]:
            j = 2 * i
            while j < n:
                j += 1
                isPrim[j] = False
    count = 0
    for i in range(2, n):
        if isPrim[i]:
            count += 1
    return count
    
if __name__ == '__main__':
    print(countPrimes_v2(6))