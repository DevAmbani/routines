class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r+= 1
            
            return s[l+1:r]
        
        for i in range(len(s)):
            even = expand(i, i)
            odd = expand(i, i+1)

            if len(even) > len(longest):
                longest = even
            if len(odd) > len(longest):
                longest = odd
        
        return longest

