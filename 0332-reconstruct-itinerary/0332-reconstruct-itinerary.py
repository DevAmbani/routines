from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itin = defaultdict(list)
        result = []

        for depart, land in sorted(tickets, reverse=True):
            itin[depart].append(land)
        
        def dfs(flight):
            
            while itin[flight]:
                nextflight = itin[flight].pop()
                dfs(nextflight)
            result.append(flight)
        
        dfs("JFK")
        return result[::-1]