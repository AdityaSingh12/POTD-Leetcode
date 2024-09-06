"""
3217. Delete Nodes From Linked List Present in Array

You are given an array of integers nums and the head of a linked list. 
Return the head of the modified linked list after removing all nodes 
from the linked list that have a value that exists in nums.
"""

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set=set(nums)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val in nums_set:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next