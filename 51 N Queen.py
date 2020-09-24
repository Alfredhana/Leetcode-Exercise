# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:34:23 2020

@author: USER
"""

def solve(n):
    res = []
    # "." 表示空 初始化棋盘
    board = ['.'*n]*n
    def isValid(row, col):
        # 检查同列冲突
        for i in range(n):
            if board[i][col] == "Q":
                return False
        # 检查右上方冲突
        i,j = row-1, col+1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i,j = i-1, j+1
        # 检查左上方冲突
        i,j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i,j = i-1, j-1
        return True
    def backtrack(row):
        # Base Case
        if row == n:
            res.append( ["".join(board[i]) for i in range(n)] )
            return True
        for col in range(n):
            # 排除不合法选择
            if isValid(row, col):
                # 做选择
                board[row] = board[row][:col]+"Q"+ board[row][col+1:]
                # 进行下一行决策
                if backtrack(row+1):
                    return True
                # 撤销选择
                board[row] = board[row][:col]+"."+ board[row][col+1:]
        return False
    backtrack(0)
    return res