class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] stores the minimum coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], 1 + dp[x - coin])

        return dp[amount] if dp[amount] != float('inf') else -1