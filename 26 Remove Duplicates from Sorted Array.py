# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:19:23 2020

@author: USER

双指针
"""

def removeDuplicates(nums):
    n = len(nums)
    if n == 0:
        return 0
    slow = 0
    fast= 1
    while fast < n:
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return nums[:slow+1]

if __name__ == '__main__':
    print(removeDuplicates([1,1,2,3,4,4,5]))