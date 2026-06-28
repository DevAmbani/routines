class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [0] * n
        parent = list(range(n))

        if n-1 != len(edges):
            return False

        def find(node):
            if node == parent[node]:
                return node
            if node != parent[node]:
                return find(parent[node])
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank [py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
            
            return True
        
        for x,y in edges:
             if union(x,y) is False:
                return False
        
        return True