import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # 2. Process unique queries in ascending order
        sorted_queries = sorted(set(queries))
        
        # Min-heap stores pairs of (interval_length, right_boundary)
        min_heap = []
        res_map = {}
        i = 0
        n = len(intervals)
        
        for q in sorted_queries:
            # Add all intervals that start at or before q
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            
            # Discard intervals that end before q (they can never cover q or future queries)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # The top of the heap is the shortest interval covering q
            res_map[q] = min_heap[0][0] if min_heap else -1
            
        # Reconstruct results matching the original order of queries
        return [res_map[q] for q in queries]