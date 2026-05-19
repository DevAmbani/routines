class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        sorted_count = sorted(count.items(), key= lambda x: x[1], reverse=True)
        ans = [item[0] for item in sorted_count]
        finalans = ans[:k]

        return finalans  