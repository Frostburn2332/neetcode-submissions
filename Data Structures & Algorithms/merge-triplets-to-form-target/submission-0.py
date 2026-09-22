from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            # Skip any triplet that has a value exceeding target at any position
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # Record matching indices
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
            
            # Early exit once all 3 positions are satisfied
            if len(good) == 3:
                return True

        return len(good) == 3