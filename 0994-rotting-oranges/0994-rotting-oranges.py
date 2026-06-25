from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append([row, col])
                if grid[row][col] == 1:
                    fresh += 1
        
        coord = [[0,1], [0,-1], [1,0], [-1,0]]
        minutes = 0
                
        while queue and fresh > 0:
            minutes += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in coord:

                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append([nr, nc])
        
        if fresh == 0:
            return minutes
        return -1
                