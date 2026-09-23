class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            result[num] = result.get(num, 0) + 1
        
        for num, count in result.items():
            freq[count].append(num)

        ans = []

        for f in range(len(freq)-1, 0, -1):
            for num in freq[f]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans 

        