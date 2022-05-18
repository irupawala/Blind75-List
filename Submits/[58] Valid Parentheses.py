from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = deque()

        for i in s:
            if i in ['(', '{', '[']: stack.append(i)  

            else:
                if not len(stack): return False # for s = "}]"                   
                x = stack.pop()
                if (x=="(" and i!=")") or (x=="{" and i!="}") or (x =="[" and i!="]"): return False

        return (len(stack) == 0)  # for s = "{["

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
