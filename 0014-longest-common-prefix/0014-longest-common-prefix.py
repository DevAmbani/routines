class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        if len(strs) == 0:
            return ""

        for i, c in enumerate(first):
            for string in strs[1:]:
                if i >= len(string) or c != string[i]:
                    return first[:i]
        
        return first
                