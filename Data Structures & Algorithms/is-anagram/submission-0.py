class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps_S={}
        maps_T={}
        
        m,n=len(s),len(t)
        maps_S={}
        maps_T={}
        if m!=n:
            return False
        for i in range(m):
            maps_S[s[i]]=1+maps_S.get(s[i],0)
            maps_T[t[i]]=1+maps_T.get(t[i],0)
        
        for c in maps_S:
            if maps_S[c]!=maps_T.get(c,0):
                return False
        
        return True

