class Solution:

    def encode(self, strs: List[str]) -> str:
        encStr = ""

        for i in strs:
            encStr += str(len(i))+"#"+i

        return encStr

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i<len(s):
            j = i
            while j<len(s) and s[j]!="#":
                j+=1

            length = int(s[i:j])
            i=j+1
            decoded.append(s[i:i+length])
            i+=length
        return decoded
    
## Other solution (shit soln)

    # def encode(self, strs: List[str]) -> str:
    #     encStr = "blahblah"

    #     for i in strs:
    #         encStr = encStr+i+"blahblah"

    #     return encStr

    # def decode(self, s: str) -> List[str]:
    #     decoded = s.split("blahblah")[1:-1]

    #     return decoded