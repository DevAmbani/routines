import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost_graph = defaultdict(list)
        dist = defaultdict(float)
        for u,v,w in times:
            cost_graph[u].append([v,w])
        
        for i in range(1, n+1):
            dist[i] = float('inf')
        dist[k] = 0

        heap = [(0, k)]  # distance, node

        while heap:
            distance, node = heapq.heappop(heap)
            if distance > dist[node]:
                continue
            
            for neighbor, cost in cost_graph[node]:
                n_dist = dist[node] + cost
                if n_dist < dist[neighbor]:
                    dist[neighbor] = n_dist
                    heapq.heappush(heap,(n_dist, neighbor))
        
        ans = -1
        for each in dist.values():
            if each == float('inf'):
                return -1
            ans = max(ans, each)
        
        return ans
