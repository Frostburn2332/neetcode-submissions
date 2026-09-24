from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res = []

        # steps: number of steps to take in the current direction
        # next_steps: number of steps for the perpendicular direction
        def dfs(next_steps: int, steps: int, r: int, c: int, dr: int, dc: int):
            if steps == 0 or next_steps == 0:
                return

            for _ in range(steps):
                r += dr
                c += dc
                res.append(matrix[r][c])

            # Turn 90° clockwise: (dr, dc) -> (dc, -dr)
            # Remaining perpendicular steps decrease by 1
            dfs(steps, next_steps - 1, r, c, dc, -dr)

        # Start at (0, -1) moving right: n horizontal steps, m vertical steps
        dfs(m, n, 0, -1, 0, 1)
        return res