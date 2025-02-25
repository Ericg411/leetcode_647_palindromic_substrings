class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 1
        palindromes = 0
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
            palindromes += 1
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    palindromes += 1
        return palindromes



        