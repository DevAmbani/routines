class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0
        lowest = prices[0]

        for r in range(len(prices)):
            lowest = min(lowest, prices[r])
            compare = prices[r] - lowest
            ans = max(ans, compare)

        return ans