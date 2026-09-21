class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_end = 0
        farthest = 0

        # Loop up to len(nums) - 1 because we never need to jump from the destination
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # When we reach the boundary of the current jump window
            if i == cur_end:
                jumps += 1
                cur_end = farthest

        return jumps