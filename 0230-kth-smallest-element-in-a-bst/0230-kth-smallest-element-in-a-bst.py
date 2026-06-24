# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def order(node):
            if not node:
                return None
            order(node.left)
            values.append(node.val)
            order(node.right)
        
        order(root)
        print(values)

        for i in range(len(values)):
            if i+1 == k:
                return values[i]