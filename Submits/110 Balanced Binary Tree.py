# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def DFS(root, height, ans):
            hl, hr = 0, 0
            
            if not root: # leaf node
                return (0, True)
            
            hl, ans_l = DFS(root.left, height, ans)
            hr, ans_r = DFS(root.right, height, ans)
            
            if not ans_l or not ans_r or abs(hl-hr) > 1: return (0, False)
            else: return (max(hl, hr)+1, True)
            
        return DFS(root, 0, True)[1]
        
'''
Time Complexity - O(logn)
Space Complexity - O(Height)

'''
