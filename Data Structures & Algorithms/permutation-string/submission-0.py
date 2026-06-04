class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)

        #CHeck if n1 > n2. Substring cannot be greater than string
        if n1>n2:
            return False
        counts_s1=[0]*26
        counts_s2=[0]*26

        # Run a loop to fill the S1 and S2 in counts. We run until S2 is the smalle string or equal to s2 at max
        for i in range(n1):
            counts_s1[ord(s1[i])-ord('a')]+=1
            counts_s2[ord(s2[i])-ord('a')]+=1
        
        #Check if the strings are equal at thehis point and return true if true initially only

        if counts_s1==counts_s2:
            return True

        #If not tru skip and run from end of n1 to n2-1
        for i in range(n1,n2):
            counts_s2[ord(s2[i])-ord('a')]+=1

            #remove the leading character
            counts_s2[ord(s2[i-n1])-ord('a')]-=1

            if counts_s1==counts_s2:
                return True
        
        #We didnt find the string return False
        return False
