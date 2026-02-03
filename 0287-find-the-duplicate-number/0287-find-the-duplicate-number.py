class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break
        
        start = 0
        while True:
            start = nums[start]
            slow = nums[slow]

            if start == slow:
                break
        
        return slow