# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return (self.count_from(root, targetSum)
           + self.pathSum(root.left, targetSum)
           + self.pathSum(root.right, targetSum))
        
    def count_from(self, node, remaining):
        if not node:
            return 0
        count = 1 if node.val == remaining else 0

        count += self.count_from(node.left, remaining - node.val)
        count += self.count_from(node.right, remaining - node.val)
        return count
