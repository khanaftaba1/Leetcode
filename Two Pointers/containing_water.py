class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights)-1

        while l < r:
            water_level = (min(heights[l],heights[r]))*(r-l)

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1

            res = max(res, water_level)
        
        return res
