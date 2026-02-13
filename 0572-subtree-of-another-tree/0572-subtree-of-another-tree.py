# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def sameTree(self, r, sR) -> bool:
        if not r and not sR:
            return True
        
        if not r or not sR:
            return False
        
        if r.val != sR.val:
            return False

        left = self.sameTree(r.left,sR.left)
        right = self.sameTree(r.right,sR.right)

        return left and right