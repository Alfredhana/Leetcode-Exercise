# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:25:40 2020

@author: USER
"""

def TwoSum_Iteration(nums, target):
    for i in range(len(nums)):
        left = nums[i+1:]
        for j in range(len(left)):
            if nums[i] + left[j] == target:
                return [i, i+1+j]

def TwoSum_HashTable_TwoPass(nums, target):
    table = {}
    for i in range(len(nums)):
        table[nums[i]] = i
    
    for i in range(len(nums)):
        if target - nums[i] in table:
            if table[target-nums[i]] != i:
                return [i, table[target-nums[i]]]
    return []

def TwoSum_HashTable_OnePass(nums, target):
    table = {}
    for i, num in enumerate(nums):
        sub = target - num
        if sub in table:
            return [table[sub], i]
        table[num] = i
    return []
    
    
def TwoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left +=  1
        elif s > target:
            right -= 1
    return [-1, -1]

if __name__ == '__main__':
    print(TwoSum_HashTable_OnePass([2,7,11,15], 9))