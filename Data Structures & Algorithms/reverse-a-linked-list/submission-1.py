# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # crnt = head
        # while crnt is not None:
        #     nextNode = crnt.next 
        #     crnt.next = prev

        #     prev=crnt
        #     crnt=nextNode
        # return prev


            





        current = head
        previous = None
        while current:
            temp_next = current.next
            current.next = previous
            previous = current 
            current = temp_next
        return previous
        