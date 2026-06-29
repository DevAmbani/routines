from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        cost_graph = defaultdict(list)
        dist = defaultdict(int)
        count = 0

        for u,v in edges:
            cost_graph[u].append([v, succProb[count]])
            cost_graph[v].append([u, succProb[count]])
            dist[count] = 0
            count += 1
        
        dist[start_node] = 1

        neighbor_heap = [(-1, start_node)]

        while neighbor_heap:
            distance, node = heapq.heappop(neighbor_heap)
            distance = -distance

            if distance < dist[node]:
                continue
            
            for neighbor, cost in cost_graph[node]:
                new_dist = dist[node] * cost
                if new_dist > dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(neighbor_heap, (-new_dist, neighbor))
            
        return dist[end_node]
