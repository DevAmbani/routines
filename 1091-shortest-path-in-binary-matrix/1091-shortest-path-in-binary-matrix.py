from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
        visited = set()
        queue = deque()
        start = [0,0,1]
        queue.append(start)
        visited.add((0,0))
        n = len(grid)-1

        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1

        while queue:
            r, c, distance = queue.popleft()
            if r == n and c == n:
                return distance
            for dr, dc in directions:
                nr , nc = r+dr, c+dc
                if (0 <= nr <= n) and (0 <= nc <= n) and ((nr,nc) not in visited) and (grid[nr][nc] == 0):
                    queue.append([nr, nc, distance+1])
                    visited.add((nr,nc))
        
        return -1
            