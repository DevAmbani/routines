class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        ans = []
        seen = set()

        for i in range(len(sorted_nums)-2):
            l = i+1
            r = len(sorted_nums) - 1
            n = sorted_nums[i]

            while l < r:
                total = sorted_nums[l] + sorted_nums[r] + n
                
                if total == 0:
                    adder = [n, sorted_nums[l], sorted_nums[r]]
                    if tuple(adder) not in seen:
                        seen.add(tuple(adder))
                        ans.append(adder)
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
            
        return ans