class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def calc(l, r):
            total = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
                total += 1
            return total
        total = 0
        for i in range(n):
            total += calc(i, i) + calc(i, i+1)
        return total
        
        