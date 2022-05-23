# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        
        pointer1, pointer2 = head, head
        
        while True:
            if pointer1.next and pointer2.next and pointer2.next.next: 
                pointer1 = pointer1.next
                pointer2 = pointer2.next.next                
            else:
                return False

            if pointer1 == pointer2: return True
            
            
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
