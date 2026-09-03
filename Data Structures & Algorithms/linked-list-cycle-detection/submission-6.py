# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def useHashMap(self, head: Optional[ListNode]) -> bool:
        # O(n) - O(n)
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return self.useHashMap(head)
        # using slow and fast pointers
        # O(n) - O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


