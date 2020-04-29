# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:36:00 2020

@author: USER
"""

def searchInsert(nums, target):
    size = len(nums)
    if size == 0:
        return 0
    
    if nums[size - 1] < target:
        return size
    
    left = 0 
    right = size - 1
    
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            return left
    return 0
    
if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 5))