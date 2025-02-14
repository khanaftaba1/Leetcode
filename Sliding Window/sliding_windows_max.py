
############# Always remember Deque is used to store the index of the elements in the array and its in decreasing order ############

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0

        while r < len(nums):

            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                res.append(nums[q[0]])
                l+=1

            r+=1

        return res


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