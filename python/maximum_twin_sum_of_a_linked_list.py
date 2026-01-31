# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = {}
        n = 0
        while head != None:
            nodes[n] = head.val
            n += 1
            head = head.next

        i = (n / 2) - 1
        j = 0
        maximum = 0
        while j <= i:
            twin = nodes[n - 1 - j]
            curr = nodes[j]
            maximum = max(maximum, twin+curr)
            j += 1
        return maximum 
            
