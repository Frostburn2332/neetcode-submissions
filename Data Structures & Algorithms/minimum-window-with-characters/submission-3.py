class Solution:

  def minWindow(self, s: str, t: str) -> str:
    if not t or not s:
      return ""

    # Frequency map of characters in t
    countT = {}
    for c in t:
      countT[c] = 1 + countT.get(c, 0)

    window = {}
    have, need = 0, len(countT)
    res, res_len = [-1, -1], float("infinity")
    l = 0

    for r in range(len(s)):
      c = s[r]
      window[c] = 1 + window.get(c, 0)

      # Check if this character fulfills the requirement for t
      if c in countT and window[c] == countT[c]:
        have += 1

      # Shrink the window from the left while it remains valid
      while have == need:
        # Update result if this window is smaller
        if (r - l + 1) < res_len:
          res = [l, r]
          res_len = r - l + 1

        # Pop from the left
        window[s[l]] -= 1
        if s[l] in countT and window[s[l]] < countT[s[l]]:
          have -= 1
        l += 1

    l, r = res
    return s[l : r + 1] if res_len != float("infinity") else ""