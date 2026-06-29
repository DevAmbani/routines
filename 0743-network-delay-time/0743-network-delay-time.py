import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        dist = defaultdict(int)
        
        for u,v,w in times:
            graph[u].append([v,w])

        for i in (range(1, n+1)):
            dist[i] = float('inf')
        
        dist[k] = 0

        heap = [(0,k)]

        while heap:
            distance, node = heapq.heappop(heap)
            if distance > dist[node]:
                continue
            
            for neighbor, weight in graph[node]:
                new_distance = dist[node] + weight
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))
        
        max_dist = max(dist.values())
        return max_dist if max_dist < float('inf') else -1