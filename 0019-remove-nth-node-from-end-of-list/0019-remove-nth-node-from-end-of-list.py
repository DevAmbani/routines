# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next
        arr.pop(len(arr)-n)

        if not arr:
            return None
        
        head = arr[0]
        curr = head
        for i in arr[1:]:
            curr.next = i
            curr = curr.next
        curr.next = None
        return head