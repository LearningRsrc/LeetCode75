# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        n = 0
        while head != None:
            nodes[n] = head.val
            n += 1
            head = head.next
        if n == 0:
            return None
        
        print(f"n before sub, loop: {n}")
        n -= 1
        reversed = ListNode(nodes[n], None)
        
        if n == 0:
            return reversed 
            
        reversed.next = ListNode(nodes[n - 1], None)
        current = reversed.next
        print(f"Nodes: {nodes}")
        print(f"reversed head: {reversed}")
        n -= 1
        while n > 0:
            print(f"n: {n}")
            print(f"current before add: {current}")
            current.next = ListNode(nodes[n - 1], None)
            current = current.next
            n -= 1
            print(f"current: {current}")
            
        return reversed
