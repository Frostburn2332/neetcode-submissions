from collections import deque
from typing import List


class Solution:

  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    output = []
    q = deque()  # stores indices of elements

    for r in range(len(nums)):
      # 1. Pop smaller elements from the back (maintain decreasing order)
      while q and nums[q[-1]] < nums[r]:
        q.pop()

      q.append(r)

      # 2. Remove indices that are out of the current window boundary
      if q[0] < r - k + 1:
        q.popleft()

      # 3. Once the window reaches size k, record the current maximum
      if r >= k - 1:
        output.append(nums[q[0]])

    return output