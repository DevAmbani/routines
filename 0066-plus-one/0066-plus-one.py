class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for k in digits:
            num = num * 10 + k

        num += 1
        return list(map(int, str(num)))
