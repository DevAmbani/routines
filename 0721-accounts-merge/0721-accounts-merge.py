from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        acc = defaultdict(list)
        parent = {}
        rank = {}

        def find(node):
            if node == parent[node]:
                return node
            elif node != parent[node]:
                return find(parent[node])
            
        def union(x,y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            
            elif rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
            return True

        for account in accounts:
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
        
        for account in accounts:
            anchor = account[1]
            for email in account[2:]:
                union(anchor, email)
        
        group = defaultdict(list)
        for account in accounts:
            for email in account[1:]:
                root = find(email)
                group[root].append(email)
        
        email_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_name[email] = name
        
        final = []
        for root, email in group.items():
            name = email_name[root]
            final.append([name] + sorted(set(email)))
        
        return final
