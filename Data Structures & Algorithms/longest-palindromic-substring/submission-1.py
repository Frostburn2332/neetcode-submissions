class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Slice returns s[l + 1 : r] because the loop overshoots by 1 on both sides
            return s[l + 1 : r]

        for i in range(len(s)):
            # Odd-length palindromes (single-character center)
            odd = expand(i, i)
            if len(odd) > len(res):
                res = odd

            # Even-length palindromes (two-character center)
            even = expand(i, i + 1)
            if len(even) > len(res):
                res = even

        return res