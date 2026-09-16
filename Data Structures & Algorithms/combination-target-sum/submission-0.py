class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        def dfs(i, currentList, total):
            if total == target:
                res.append(currentList.copy())
                return
            if total > target or i >= len(nums):
                return
            
            currentList.append(nums[i])

            dfs(i, currentList, total + nums[i])

            currentList.remove(nums[i])

            dfs(i + 1, currentList, total)

        dfs(0, [], 0)
        return res


