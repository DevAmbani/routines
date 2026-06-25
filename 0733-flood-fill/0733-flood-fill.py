class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        columns = len(image[0])
        ogcolor = image[sr][sc]

        if ogcolor == color:
            return image

        def dfs(sr, sc):
            if sr < 0 or sr >= rows:
                return
            if sc < 0 or sc >= columns:
                return
            if image[sr][sc] != ogcolor:
                return          
            if image[sr][sc] == ogcolor:
                image[sr][sc] = color
            
            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)
            
        dfs(sr, sc)

        return image
        