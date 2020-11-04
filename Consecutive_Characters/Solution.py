class Solution:
    def maxPower(self, s: str) -> int:
        
        total = 1
        high = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                total += 1
            else: 
                total = 1
            high = max(high, total)
        
        return high
