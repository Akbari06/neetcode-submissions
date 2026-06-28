class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != "O" or
                (r, c) in visit
            ):
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Step 1: Run DFS from border 'O's
        for r in range(ROWS):
            for c in [0, COLS - 1]:
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(COLS):
            for r in [0, ROWS - 1]:
                if board[r][c] == "O":
                    dfs(r, c)

        # Step 2: Flip all unvisited 'O's to 'X', and keep visited 'O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"

        
        