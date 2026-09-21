from functools import cache
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        @cache
        def dfs(i: int, cur_target: int) -> bool:
            if cur_target == 0:
                return True
            if cur_target < 0 or i >= len(nums):
                return False

            # Try skipping nums[i] or taking nums[i]
            return dfs(i + 1, cur_target) or dfs(i + 1, cur_target - nums[i])

        return dfs(0, target)