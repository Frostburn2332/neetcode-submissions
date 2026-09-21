from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i, j + 1) + dfs(i + 1, j)

        return dfs(0, 0)