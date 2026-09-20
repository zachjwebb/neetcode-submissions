class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i, j in enumerate(nums):
            check = target - j
            if check in tmp:
                return [tmp[check], i]
            tmp[j] = i
        return []