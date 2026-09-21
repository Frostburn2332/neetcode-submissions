class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Ensure word2 is the shorter string to optimize space
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        m, n = len(word1), len(word2)
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            next_dp = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    next_dp[j] = dp[j - 1]
                else:
                    next_dp[j] = 1 + min(
                        dp[j],          # Delete
                        next_dp[j - 1], # Insert
                        dp[j - 1]       # Replace
                    )
            dp = next_dp

        return dp[n]