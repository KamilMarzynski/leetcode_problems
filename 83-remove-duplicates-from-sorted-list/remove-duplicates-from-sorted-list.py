# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            next_node = curr.next
            while curr.val == next_node.val:
                if next_node.next:
                    next_node = next_node.next
                else:
                    curr.next = None
                    return head

            curr.next = next_node

            if curr.next:
                curr = curr.next
            else:
                return head
        
        return head