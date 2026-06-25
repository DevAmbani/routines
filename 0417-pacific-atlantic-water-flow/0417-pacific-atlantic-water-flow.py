from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        poq = deque()
        aoq = deque()

        def bfs(queue):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            visited = set(queue)
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        
                        if 0 <= nr < rows and 0 <= nc < cols and heights[r][c] <= heights[nr][nc] and (nr,nc) not in visited:
                            queue.append([nr, nc])
                            visited.add((nr,nc))
            return visited

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    poq.append((row, col))
                if row == rows-1 or col == cols-1:
                    aoq.append((row, col))
        
        pacific = bfs(poq)
        atlantic = bfs(aoq)
        ans = []

        for element in pacific:
            if element in atlantic:
                ans.append(element)
        
        return ans
        