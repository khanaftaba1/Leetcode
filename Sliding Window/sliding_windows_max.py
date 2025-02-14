






############# other solution ################

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        res = []

        for i in range(k):
            window.append(nums[i])

        l = 0
        for r in range(k,len(nums)):

            res.append(max(window))
            window.append(nums[r])
            window.pop(0)

            l+=1
        
        res.append(max(window))

        return res