class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # length is the window size between boundaries i and j
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                # k is the last balloon to burst between i and j
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    )

        return dp[0][n - 1]