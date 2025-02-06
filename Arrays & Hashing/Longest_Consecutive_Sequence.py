


####### Other Solutions ####### (issue is we sort here which takes O(nlogn) time)

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

#         if nums == []:
#             return 0

#         new_nums = sorted(set(nums))
#         res = 0
#         new_res = 1
        
#         for i in range(1,len(new_nums)):
#             if new_nums[i-1] == new_nums[i]-1:
#                 new_res+=1
#             else:
#                 res =  max(new_res,res)
#                 new_res = 1
#         res = max(new_res, res)
#         return res