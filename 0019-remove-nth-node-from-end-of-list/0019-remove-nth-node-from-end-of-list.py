# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        number = count - n
        n_count = 1

        if number == 0:
            return head.next

        curr = head
        while curr and curr.next:
            if n_count == number:
                curr.next = curr.next.next
                break
            n_count += 1
            curr = curr.next
        
        return head