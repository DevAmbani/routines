class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        for c in t:
            count[c] += 1

        new = defaultdict(int)
        l = 0
        ans = ""
        min_len = float("inf")

        for r in range(len(s)):
            new[s[r]] += 1

            while all(new[c] >= count[c] for c in count):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]
                new[s[l]] -= 1
                l += 1

        return ans