class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def count_palindromes(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            # Odd-length palindromes (single-character center)
            res += count_palindromes(i, i)
            # Even-length palindromes (two-character center)
            res += count_palindromes(i, i + 1)

        return res