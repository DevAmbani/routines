class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        total = 0

        def backtrack(state, start, total):
            if total == target:
                ans.append(state[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                state.append(candidates[i])
                total = sum(state)
                backtrack(state, i, total)
                state.pop()
        
        backtrack([], 0, 0)
        return ans
    