# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:57:27 2020

@author: USER
"""

def solve(n):
    # 生成N*N的棋盘，填充棋盘，每个格子默认是“。”表示没有放置皇后
    board = [["." for _ in range(n)] for _ in range(n)]
    res = []
    # 检查当前的行和列是否可以放置皇后
    def check(row, col):
        # 检查竖着的一列是否有皇后
        for i in range(row):
            if board[i][col]=="Q":
                return False
        # 检查左下到右上的斜边是否有皇后    
        i,j = row-1,col+1
        while i>=0 and j<n:
            if board[i][j]=="Q":
                return False
            i,j = i-1,j+1
        # 检查左上到右下的斜边是否有皇后        
        i,j = row-1,col-1
        while i>=0 and j>=0:
            if board[i][j]=="Q":
                return False
            i,j = i-1,j-1
        return True
    def backtrack(row):
        # x是从0开始计算的
        # 当x==n时所有行的皇后都放置完毕，此时记录结果
        if row==n:
            res.append( ["".join(board[i]) for i in range(n)] )
            return 
        # 遍历每一列    
        for col in range(n):
            # 检查[x,y]这一坐标是否可以放置皇后
            # 如果满足条件，就放置皇后，并继续检查下一行
            if check(row,col):
                board[row][col] = "Q"
                backtrack(row+1)
                board[row][col] = "."
    backtrack(0)
    return res
    