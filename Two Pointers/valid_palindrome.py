class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1

        while l < r :
            while l < r and self.checkChar(s[l]):
                l+=1
            while l < r and self.checkChar(s[r]):
                r-=1   
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        
        return True

    
    def checkChar(self, c):
        if (ord("a")<=ord(c)<=ord("z") or 
            ord("A")<=ord(c)<=ord("Z") or 
            ord("0")<=ord(c)<=ord("9")):
            return False
        return True
    
########## other solution ##########

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

#         for i in range(len(newS)//2):
#             if newS[i] != newS[len(newS)-i-1]:
#                 return False
        
#         return True