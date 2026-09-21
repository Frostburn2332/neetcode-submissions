from collections import deque
from typing import List


class Solution:

  def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()

    # 1. Add all treasure chests (0s) to the queue
    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == 0:
          q.append((r, c))

    # 2. Multi-source BFS outward from all chests simultaneously
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
      r, c = q.popleft()

      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        # Check bounds and only visit unvisited empty rooms (INF = 2147483647)
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
          grid[nr][nc] = grid[r][c] + 1
          q.append((nr, nc))