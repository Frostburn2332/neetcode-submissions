class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            # If current index is beyond the furthest reachable point, we are stuck
            if i > max_reach:
                return False

            # Update the furthest index we can reach
            max_reach = max(max_reach, i + jump)

            # Early exit if we can already reach or pass the last index
            if max_reach >= len(nums) - 1:
                return True

        return True