"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        mp = {None:None}

        while curr:
            copyNode = Node(curr.val)
            mp[curr] = copyNode
            curr = curr.next

        curr = head
        while curr:
            copyNode = mp[curr]
            copyNode.next = mp[curr.next]
            copyNode.random = mp[curr.random]
            curr = curr.next
        
        return mp[head]