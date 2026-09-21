class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        leftMax_arr = [0] * n
        rightMax_arr = [0] * n

        leftMax_arr[0] = height[0]
        for i in range(1, n):
            leftMax_arr[i] = max(leftMax_arr[i-1], height[i])

        rightMax_arr[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax_arr[i] = max(rightMax_arr[i+1], height[i])

        for i in range(n):
            res += min(leftMax_arr[i], rightMax_arr[i]) - height[i]
        return res