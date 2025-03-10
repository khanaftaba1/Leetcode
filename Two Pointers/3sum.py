class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0 or a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                check = a+nums[l]+nums[r]
                if check < 0:
                    l+=1
                elif check > 0:
                    r-=1
                elif check == 0:
                    res.append([nums[l],nums[r],a])
                    l+=1
                while nums[l]==nums[l-1] and l < r:
                    l+=1
        
        return res