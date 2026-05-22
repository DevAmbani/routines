class Solution:
    def isValid(self, s: str) -> bool:
        adder = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                adder.append(c)
            elif c == ")":
                if not adder or adder[-1] != "(":
                    return False
                else:
                    adder.pop()
            elif c == "}": 
                if not adder or adder[-1] != "{":
                    return False
                else:
                    adder.pop()
            elif c == "]": 
                if not adder or adder[-1] != "[":
                    return False
                else:
                    adder.pop()
        
        return len(adder) == 0
