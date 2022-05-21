# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, root, key):
        if not root:
            return False
        
        elif root.val == key.val:
            return True
        
        elif root.val > key.val:
            return self.find(root.left, key)
        
        elif root.val < key.val:
            return self.find(root.right, key)
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #print(type(root.val))
        #print(type(p.val))
        #print(type(q.val))
        
        if not root: return None
        
        node_l = self.lowestCommonAncestor(root.left, p, q)
        if node_l: return node_l
        
        node_r = self.lowestCommonAncestor(root.right, p, q) 
        if node_r: return node_r
        
        if self.find(root, p) and self.find(root,q):
            return root 
        
'''
Time Complexity - O(logn)
Space Complexity - O(1)
'''
