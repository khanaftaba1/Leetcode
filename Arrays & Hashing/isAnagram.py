from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic_1 = defaultdict(int)
        dic_2 = defaultdict(int)

        for char in s:
            dic_1[char] += 1
        
        for char in t:
            dic_2[char] += 1

        for key in dic_1:
            if key not in dic_2 or dic_1[key] != dic_2[key]:
                return False
        
        return True
    
##### other solution

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         counts, countT = {}, {}

#         for i in range(len(s)):
#             counts[s[i]] = 1 + counts.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)

##### instead of the below code u can also just compare like "return countS == countT"

#         for c in counts:
#             if counts[c] != countT.get(c, 0):
#                 return False

#         return True

##### other solution super inefficient bcoz t makes new string everytime

        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)):
        #     if s[i] not in t:
        #         return False
        #     t = t.replace(s[i],"",1)

        # return True