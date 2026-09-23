from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals primarily by end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # If current interval overlaps with the previous chosen one,
            # remove the current one (increment removals)
            if start < prev_end:
                removals += 1
            else:
                # No overlap; keep this interval and update the end boundary
                prev_end = end

        return removals