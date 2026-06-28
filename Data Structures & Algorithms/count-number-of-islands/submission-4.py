class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            # Check bounds and if it's water or already visited
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return

            visited.add((r, c))

            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)

        return res