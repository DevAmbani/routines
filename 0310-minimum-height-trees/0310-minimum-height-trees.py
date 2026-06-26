from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degrees = [0] * n
        count = defaultdict(list)

        if n==1:
            return [0]

        for a,b in edges:
            count[a].append(b)
            count[b].append(a)
            degrees[a] += 1
            degrees[b] += 1

        queue = deque()
        for i in range(len(degrees)):
            if degrees[i] == 1:
                queue.append(i)
        
        num_elements_left = n
        while num_elements_left > 2:
            num_elements_left = num_elements_left - len(queue)

            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbors in count[node]:
                    degrees[neighbors] -= 1
                    if degrees[neighbors] == 1:
                        queue.append(neighbors)

        return list(queue)
        