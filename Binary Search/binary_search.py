class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while r >= l:
            m = l + ((r-l)//2) # we could use (l+r)//2 but i java and C++ can have overflow issue

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1