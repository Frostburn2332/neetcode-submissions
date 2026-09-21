class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # An empty target can always be formed 1 way

        for char in s:
            # Traverse backward to ensure dp[j - 1] represents the state before this character
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]