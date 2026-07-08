class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []

        def backtrack(state):
            if (state not in ans) and (len(state) == len(nums)):
                ans.append(state[:])
            
            for i in range(len(nums)):
                if nums[i] in state:
                    continue 
                state.append(nums[i])
                backtrack(state)
                state.pop()

        backtrack([])
        return ans