class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = []
        for string in strs:
            result.append(f"{len(string)}#{string}")
        
        return "".join(result)
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            
            length= int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
        
               