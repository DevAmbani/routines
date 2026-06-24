from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        values = []
        def order(node):   
            if node.left:
                order(node.left)
            values.append(node.val)
            if node.right:
                order(node.right)
        
        order(root)
        print(values)
        for i in range(len(values)-1):
            if (values[i] >= values[i+1]):
                return False
        
        return True