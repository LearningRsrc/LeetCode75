# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = self.dfs(root, root.val)
        return ans

    def dfs(self, node, max_sofar):
        if not node:
            return 0
        is_good = node.val >= max_sofar
        count = 1 if is_good else 0
        new_max = max(max_sofar, node.val)
        count += self.dfs(node.right, new_max)
        count += self.dfs(node.left, new_max)
        return count
