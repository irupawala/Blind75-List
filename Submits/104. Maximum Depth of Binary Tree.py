# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth, max_depth = 1, 1
        
        def InOrderTraversal(node, depth, max_depth):
            if not node.left and not node.right:
                return depth
            if node.left:
                max_depth = max(InOrderTraversal(node.left, depth+1, max_depth), max_depth)
            if node.right:
                max_depth = max(InOrderTraversal(node.right, depth+1, max_depth), max_depth)        
            return max(InOrderTraversal(node.left, depth+1, max_depth), max_depth)
        
        return InOrderTraversal(root, depth, max_depth)
    
'''
Time Complexity - log(n)
Space Complexity - O(1)
'''
