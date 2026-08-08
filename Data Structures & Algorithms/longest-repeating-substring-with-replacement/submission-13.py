class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {}

        l, result = 0, 0

        for r in range(len(s)):
            charFreq[s[r]] = charFreq.get(s[r], 0) + 1

            while (r - l + 1) - max(charFreq.values()) > k:
                charFreq[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        return result