class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        n=len(s)
        seen=set()
        for r in range(n):
            #If substring is valid which means that char is in set(as set shouldnt have duplicate chars)
            while s[r] in seen:
                seen.remove(s[l]) #remove  thhe left pointer string
                l+=1
            
            w=(r-l)+1
            longest=max(longest,w)
            seen.add(s[r]) # we append the right substring since thts not in the set

        return longest
