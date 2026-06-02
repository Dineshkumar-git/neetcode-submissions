class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result = 0
        for char in s+t:
            result ^= ord(char)

        return result == 0 and sorted(s) == sorted(t)