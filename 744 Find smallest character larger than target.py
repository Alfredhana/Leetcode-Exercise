# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:50:10 2020

@author: USER
"""

def searchSmallest(letters, target):
    size = len(letters);
    l = 0;
    r = size - 1;
    while (l <= r):
        mid = (r + l) // 2
        if (target < letters[mid]):
            r = mid - 1;
        else:
            l = mid + 1
    return letters[l] if l < r else letters[0]
        
    
if __name__ == '__main__':
    print(searchSmallest(["c", "f", "j"], 'f'))