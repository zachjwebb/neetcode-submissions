class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sh = {}
        th = {}
        for c in range(len(s)):
            sh[s[c]] = sh.get(s[c], 0) + 1
            th[t[c]] = th.get(t[c], 0) + 1
        if sh == th:
            return True
        return False