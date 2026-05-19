class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        forward = [1] * len(nums)
        reverse = [1] * len(nums)
        ans = [1] * len(nums)

        for i in range(len(nums)):
            forward[i] = prefix
            prefix *= nums[i]
            

        for i in range(len(nums)-1, -1, -1):
            reverse[i] = suffix
            suffix *= nums[i]
            

        for i in range(len(nums)):
            ans[i] = forward[i] * reverse[i]

        print(forward)
        print(reverse)
        return ans