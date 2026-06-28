class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()
        res=[]
        
        def dfs(r,c,prevHeight,wSet):
            if (r<0 or r == ROWS or c<0 or c==COLS or (r,c) in wSet or heights[r][c] < prevHeight):
                return 
            wSet.add((r,c))
            dfs(r+1, c, heights[r][c], wSet)
            dfs(r-1, c, heights[r][c], wSet)
            dfs(r, c+1, heights[r][c], wSet)
            dfs(r, c-1, heights[r][c], wSet)
        
        for c in range(COLS):
            dfs(0,c,heights[0][c],pac)
            dfs(ROWS-1,c,heights[ROWS-1][c],atl)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0],pac)
            dfs(r, COLS-1, heights[r][COLS-1],atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res