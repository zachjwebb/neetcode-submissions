class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set(nums)
        longest = 0
        for num in track:
            if (num - 1) not in track:
                answer = 1
                while (num + answer) in track:
                    answer += 1

                longest = max(longest, answer)
        return longest
                



