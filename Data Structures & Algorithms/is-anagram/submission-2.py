class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = list(s)

        if len(s) != len(t):
            return False

        for char in t:
            if char in sArray:
                sArray.remove(char)
            else: 
                return False

        return True