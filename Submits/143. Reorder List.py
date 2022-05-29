# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
    def lenList(self, head):
        counter = 1
        
        while head.next:
            counter += 1
            head = head.next
        
        return counter
    
    def createTwoHalfLists(self, head, half_len):
        head_first_list, counter = head, 1
        
        while counter != half_len:
            counter += 1
            head = head.next
            
        head_second_list = head.next
        head.next = None
        return head_first_list, head_second_list
    
    def reverseList(self, head):
        previous, current, next = None, head, None
        
        while current:
            _node = current.next
            current.next = previous
            previous = current 
            current = _node
        
        return previous
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        list_len = self.lenList(head)
        if list_len == 1: return head
        
        half_len = list_len // 2
        first_head, second_head = self.createTwoHalfLists(head, half_len)
        
        reverse_second_head = self.reverseList(second_head)
        second_head = None
        
        while first_head and reverse_second_head:
            first_head_next, reverse_second_head_next = first_head.next, reverse_second_head.next
            first_head.next = reverse_second_head
            reverse_second_head.next = first_head_next
            
            first_head = first_head_next
            if not first_head:
                reverse_second_head.next = reverse_second_head_next
                reverse_second_head, reverse_second_head_next = None, None
            else:
                reverse_second_head = reverse_second_head_next
            
        
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''    
    
    
