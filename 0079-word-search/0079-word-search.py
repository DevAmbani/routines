class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        q = deque(word)
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[0]):
                return False     
            if (row, col) in visited:
                return False

            if word[index] != board[row][col]:
                return False
            
            visited.add((row, col))
            
            found = dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1)

            visited.remove((row, col))

            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        
        return False
              