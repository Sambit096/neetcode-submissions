# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #store the root val into d so we can return the list at the end
        d=ListNode()
        #THis is the pointer well need to move
        cur=d

        while list1 and list2:
            if list1.val<list2.val:
                cur.next=list1
                cur=list1
                list1=list1.next
            #Directly check the greater than or less than no need to check equals
            else:
                cur.next=list2
                cur=list2
                list2=list2.next
        
        #Etither list 1 is null or list 2 is null or both are none. 
        cur.next=list1 if list1 else list2
        return d.next

