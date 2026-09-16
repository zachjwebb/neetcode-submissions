class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        resultCount = {}

        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            resultCount[num] = resultCount.get(num, 0) + 1

        for num,count in resultCount.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res)== k:
                    return res
        
        

        

        
        



        
        