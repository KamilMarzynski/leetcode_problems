# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
    
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current = slow
        reversed_list = None

        while current:
            next_node = current.next
            current.next = reversed_list
            reversed_list = current
            current = next_node

        current = head
        while reversed_list:
            if reversed_list.val != current.val:
                return False
            reversed_list = reversed_list.next
            current = current.next
        
        return True