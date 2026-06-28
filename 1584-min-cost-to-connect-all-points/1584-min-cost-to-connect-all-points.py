class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        rank = [0] * n

        def find(node):
            if node == parent[node]:
                return node
            if node != parent[node]:
                return find(parent[node])
        
        def union(x,y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
            
            return True
        
        cost = []
        for i in range(n):
            for j in range(i+1, n):
                price = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                cost.append([price, i, j])
        
        cost.sort()
        ans = 0

        for price, i, j in cost:
            if union(i, j):
                ans += price
        
        return ans