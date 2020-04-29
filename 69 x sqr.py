# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:04:44 2020

@author: USER
"""

"""
二分查找
使用二分法搜索平方根的思想
高了就往低了猜
低了就往高了猜
范围越来越小
"""

def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    left = 1
    right = x // 2 + 1
    print("right value:{}".format( rightq))
    while left < right:
        mid = (left + right + 1) >> 1
        print("Mid value:{}".format( mid))
        square = mid * mid
        if square > x:
            right = mid - 1
        else:
            left = mid
    return left
        
    
if __name__ == '__main__':
    print(mySqrt(8))