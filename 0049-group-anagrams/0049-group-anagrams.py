class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            final[key].append(word)

        return list(final.values())
        
        