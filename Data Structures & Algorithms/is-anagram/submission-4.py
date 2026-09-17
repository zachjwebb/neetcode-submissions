class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        th , sh = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            th[t[i]] = 1 + th.get(t[i], 0)
            sh[s[i]] = 1 + sh.get(s[i], 0)
        
        if th == sh:
            return True

        return False