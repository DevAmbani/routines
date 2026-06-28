class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        components = n

        def find(node):
            if parent[node] == node:
                return node
            elif parent[node] != node:
                return find(parent[node])
        
        def union(x, y):
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
        
        for x,y in edges:
            if union(x,y):
                components -= 1
        
        return components