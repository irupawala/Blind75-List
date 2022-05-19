# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS

from collections import deque

# Ibrahim Iterative
'''
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
            return max_depth
        
        return InOrderTraversal(root, depth, max_depth)
'''    

# BFS
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        qmain = deque()
        max_depth = 0
        qmain.append(root)
        
        while qmain:   
            for i in range(len(qmain)):
                node = qmain.popleft()
                if node.left: qmain.append(node.left)
                if node.right: qmain.append(node.right)
            max_depth += 1
        return max_depth
'''
    
    
# ITERATIVE DFS   
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
        
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res    
'''  
    
    
'''
Time Complexity - log(n)
Space Complexity - O(1)
'''


