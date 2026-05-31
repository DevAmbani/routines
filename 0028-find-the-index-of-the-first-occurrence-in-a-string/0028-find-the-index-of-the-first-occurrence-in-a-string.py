class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        check_len = len(needle)

        for i in range(len(haystack)):
            if haystack[i:i+check_len] == needle:
                return i
        
        return -1
                