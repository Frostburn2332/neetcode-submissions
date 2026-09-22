class Solution:
    def checkValidString(self, s: str) -> bool:
        c_min = 0  # Minimum possible open brackets needed
        c_max = 0  # Maximum possible open brackets needed

        for ch in s:
            if ch == '(':
                c_min += 1
                c_max += 1
            elif ch == ')':
                c_min -= 1
                c_max -= 1
            else:  # ch == '*'
                c_min -= 1
                c_max += 1

            # Too many ')' encountered; even '*' cannot save it
            if c_max < 0:
                return False

            # c_min cannot be negative (a '*' can just be empty rather than ')')
            c_min = max(c_min, 0)

        # Valid if it is possible to balance out to exactly 0
        return c_min == 0