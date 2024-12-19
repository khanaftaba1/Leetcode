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


#### Other solution

# numbers = [1, 2, 3, 4]

# def duplicates(nums):
    
#     dic = {}
    
#     for i in nums:
#         dic[i] = dic.get(i, 0) + 1
#         if dic[i]>1:
#             return True
    
#     return False

# print(duplicates(numbers))