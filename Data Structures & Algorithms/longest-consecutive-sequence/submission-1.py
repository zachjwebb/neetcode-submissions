class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in check:
                ans = 1
                while (num + ans) in check:
                    ans += 1
                
                res = max(res, ans)
        
        return res
            
