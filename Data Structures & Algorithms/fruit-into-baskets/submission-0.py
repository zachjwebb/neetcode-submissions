class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ch = {}
        l = 0
        res = 0
        for r in range(len(fruits)):
            ch[fruits[r]] = ch.get(fruits[r], 0) + 1
            while len(ch) > 2:
                ch[fruits[l]] -= 1
                if ch[fruits[l]] == 0:
                    del ch[fruits[l]]         
                l += 1
            res = max(res, r - l + 1)
        return res
        
        