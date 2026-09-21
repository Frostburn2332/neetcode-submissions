class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices of bars in strictly increasing height order
        max_area = 0
        n = len(heights)

        for i in range(n):
            # When the current bar is shorter than the bar at stack[-1],
            # the bar at stack[-1] cannot extend further right.
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # If stack is empty, the rectangle spans from index 0 to i - 1
                # Otherwise, it spans from stack[-1] + 1 to i - 1
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        # Process any remaining bars in the stack
        while stack:
            h = heights[stack.pop()]
            w = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, h * w)

        return max_area