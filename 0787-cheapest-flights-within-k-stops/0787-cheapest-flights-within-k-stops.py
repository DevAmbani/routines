from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = defaultdict(int)
        for i in range(n):
            dist[i] = float('inf')
        dist[src] = 0

        for _ in range(k+1):
            temp = dist.copy()
            for sour, dest, cost in flights:
                if temp[dest] > dist[sour] + cost:
                    temp[dest] = dist[sour] + cost
            dist = temp

        if dist[dst] == float('inf'):
            return -1
        return dist[dst]