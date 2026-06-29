class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = []

        for rows in range(n):
            row = []
            for cols in range(n):
                if rows == cols:
                    row.append(0)
                else:
                    row.append(float('inf'))
            matrix.append(row)

        for src, dest, cost in edges:
            matrix[src][dest] = cost
            matrix[dest][src] = cost
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        
        ans = -1
        ans_count = float('inf')
        for row in range(n):
            count = 0
            for col in range(n):
                if matrix[row][col] <= distanceThreshold:
                    count += 1
            
            if count <= ans_count:
                ans_count = count
                ans = row
        
        return ans

