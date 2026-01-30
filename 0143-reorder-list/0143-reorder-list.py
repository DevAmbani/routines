# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        back = slow.next
        slow.next = None  # keep front stream intact

        while back:
            nxt = back.next
            back.next = prev
            prev = back
            back = nxt

        # Weave: front (head) and back (prev)
        front = head
        back = prev
        while back:
            n1 = front.next
            n2 = back.next

            front.next = back
            back.next = n1

            front = n1
            back = n2
            
        
        
        