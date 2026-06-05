from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        #Counter for the number of time elements appearing in the List
        counter=Counter(nums)
        #bucket of the list size
        buckets=[[] for _ in range(n+1)]

        #Go through the dictionary(number is the numeber and frequency is the index)
        for num,freq in counter.items():
            #Check if index of bucket is 0 then put that number in as a list
            if buckets[freq]==0:
                buckets[freq]=[num]
            
            else:
                buckets[freq].append(num)
            
        res=[]

        for i in range(n,-1,-1):
            if buckets[i]!=0:
                res.extend(buckets[i])
            #Check if len of res == k and break
            if len(res)==k:
                break
        
        return res

