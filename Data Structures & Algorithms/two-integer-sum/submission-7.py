class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in track:
                return [track[diff], i]
            track[n] = i
        return []
        