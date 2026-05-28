class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = ""
        for c in s:
            if c not in window:
                window += c
                length = len(window)
                longest = max(longest, length)
            else:
                while c in window:
                    window = window[1:]
                window += c

        return longest