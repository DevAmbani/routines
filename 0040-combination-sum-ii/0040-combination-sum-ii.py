class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        state = []
        candidates.sort()

        def backtrack(start, state, total):
            if (total == target) and (state not in ans):
                ans.append(state[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i != start and candidates[i] == candidates[i-1]:
                    continue
                state.append(candidates[i])
                backtrack(i+1, state, total + candidates[i])
                state.pop()
        
        backtrack(0, [], 0)
        return ans
        