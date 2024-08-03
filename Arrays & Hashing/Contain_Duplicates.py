from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        dic = defaultdict(int)

        for i in nums:
            dic[i]+=1
            if dic[i]>=2:
                return True
        
        return False
    
#### Other solution

# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False