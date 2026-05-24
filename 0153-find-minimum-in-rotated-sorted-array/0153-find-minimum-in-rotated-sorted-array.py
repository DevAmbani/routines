class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]

        for n in nums:
            ans = min(ans, n)

        return ans
        