class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        longest = 0
        freq = 0

        for r in range(len(s)):
            count[s[r]] += 1
            freq = max(freq, count[s[r]])

            while (r-l+1)-freq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, (r-l+1))
        
        return longest