# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        arr=[]
        cur =head
        #Put the stuff into the arr
        while cur:
            arr.append(cur)
            cur=cur.next
        
        l,r=0,len(arr)-1

        #Move through the list with the array incides la nd r
        while l<r:
            arr[l].next=arr[r]
            l+=1
            if l==r:
                break
            arr[r].next=arr[l]
            r-=1
        arr[l].next=None
