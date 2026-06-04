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
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        prev = None

        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        curr = head
        while curr and prev and prev.next:
            temp1 = curr.next
            temp2 = prev.next
            curr.next = prev
            prev.next = temp1

            curr = temp1
            prev = temp2

        return head