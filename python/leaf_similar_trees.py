# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        answer = []
        def dfs(root):
            if root == None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 and right == -1:
                answer.append(root.val)
            return answer

        leaf1 = dfs(root1) 
        answer = []
        leaf2 = dfs(root2)
        if leaf1 == leaf2:
            return True
        else:
            return False
