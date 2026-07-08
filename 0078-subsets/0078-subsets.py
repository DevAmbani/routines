class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(state, start):
            result.append(state[:])
            
            for i in range(start, len(nums)):
                state.append(nums[i])
                backtrack(state, i+1)
                state.pop()
        
        backtrack([], 0)

        return result