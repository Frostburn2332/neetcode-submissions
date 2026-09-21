from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[i] represents whether s[i:] can be segmented
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                w_len = len(w)
                if i + w_len <= n and s[i : i + w_len] == w:
                    if dp[i + w_len]:
                        dp[i] = True
                        break

        return dp[0]