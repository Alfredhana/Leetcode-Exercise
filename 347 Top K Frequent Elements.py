# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:30:57 2020

@author: USER
"""
import collections
import heapq

class Solution:
  def topKFrequent(self, nums, k):
    counts = collections.Counter(nums)
    h = []
    for num in counts.keys():
      heapq.heappush(h, (counts[num], num))
      if len(h) > k: heapq.heappop(h)
    return [heapq.heappop(h)[1] for i in range(k)]

if __name__ == "__main__":
    Solution.topKFrequent([1,1,2,3,4,4,4], 2)
