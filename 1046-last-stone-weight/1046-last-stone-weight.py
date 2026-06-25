import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
        
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, first-second)
        
        if len(heap) == 0:
            return 0
        
        return -heapq.heappop(heap)
        