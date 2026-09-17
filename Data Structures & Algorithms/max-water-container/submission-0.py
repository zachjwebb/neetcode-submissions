class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        h = 0
        width = 0
        ans = 0
        while l < r:
            h = min(heights[l], heights[r])
            width = r-l
            ans = max(h * width, ans)
            if (heights[l] < heights[r]):
                l+= 1
            else:
                r-=1
        return ans