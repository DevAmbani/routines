class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        elements = len(grid[0])
        maxarea = 0

        def dfs(row, element):
            if row < 0 or row >= rows:
                return 0
            if element < 0 or element >= elements:
                return 0
            if grid[row][element] == 0:
                return 0
            
            grid[row][element] = 0
            
            return 1 + dfs(row+1, element) + dfs(row-1, element) + dfs(row, element+1) + dfs(row, element-1)

        for row in range(len(grid)):
            for element in range(len(grid[0])):
                if grid[row][element] == 1:
                    area = dfs(row, element)
                    maxarea = max(maxarea, area)
        
        return maxarea
        