class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac_reachable = set()
        atl_reachable = set()

        def dfs(r: int, c: int, reachable: set):
            reachable.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                # Check bounds, avoid revisits, and ensure height is non-decreasing (uphill)
                if (0 <= nr < ROWS and 0 <= nc < COLS 
                    and (nr, nc) not in reachable 
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        # 1. Traverse uphill starting from coastal edges
        for r in range(ROWS):
            dfs(r, 0, pac_reachable)          # Pacific (left edge)
            dfs(r, COLS - 1, atl_reachable)    # Atlantic (right edge)

        for c in range(COLS):
            dfs(0, c, pac_reachable)          # Pacific (top edge)
            dfs(ROWS - 1, c, atl_reachable)    # Atlantic (bottom edge)

        # 2. Cells reached from both oceans form the solution
        return list(pac_reachable & atl_reachable)