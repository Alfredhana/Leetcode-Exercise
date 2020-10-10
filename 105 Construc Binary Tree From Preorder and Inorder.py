# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:48:51 2020

@author: USER
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def buildTree(preorder, inorder):
    return build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

def build(preorder, preStart, preEnd, inorder, inStart, inEnd):
    if preStart > preEnd:
        return None
    rootVal = preorder[preStart]
    index = 0
    for i in range(inStart, inEnd+1):
        if inorder[i] == rootVal:
            index = i
            break
    root = TreeNode(rootVal)
    leftSize = index - inStart
    root.left = build(preorder, preStart+1, preStart+leftSize, inorder, inStart, index-1)
    root.right = build(preorder, preStart+leftSize+1, preEnd, inorder, index+1,inEnd)
    return root

def printTree(root):
    queue = []
    result = []
    if root == None:
        return result

    queue.append(root)
    while queue:
        newNode = queue.pop(0)
        result.append(newNode.val)
        if newNode.left != None:
            queue.append(newNode.left)
        if newNode.right != None:
            queue.append(newNode.right)
    return result

if __name__ == "__main__":
    root = buildTree([3,9,20,15,7],[9,3,15,20,7])
    