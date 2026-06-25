class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        elements = len(grid[0])

        def dfs(row, element):
            if row >= rows or row < 0:
                return
            if element >= elements or element < 0:
                return
            if grid[row][element] == '0':
                return
            
            if grid[row][element] == '1':
                grid[row][element] = '0'

            dfs(row+1, element)
            dfs(row-1, element)      
            dfs(row, element+1)
            dfs(row, element-1)

        for row in range(len(grid)):
            for element in range(len(grid[0])):
                if grid[row][element] == '1':
                    count += 1
                    dfs(row, element)
        
        return count