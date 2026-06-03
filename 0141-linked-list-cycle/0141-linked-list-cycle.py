# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = head
        curr2 = head

        while curr2 and curr2.next:
            s1 = curr1.next
            s2 = curr2.next.next

            if s1 == s2:
                return True
            
            curr1 = curr1.next
            curr2 = curr2.next.next
        
        return False