# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr=head
        arr = []
        while curr:
            if curr.next == None:
                return False 

            arr.append(curr.next)
            curr = curr.next

            if curr.next in arr:
                return True

        return False       
