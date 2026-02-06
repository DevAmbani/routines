class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(0,x+1):
            if (i*i) > x:
                return i-1
            elif (i*i) == x:
                return i