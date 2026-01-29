# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        i = 1
        odd_head = ListNode()
        even_head = ListNode()
        current_odd_node = ListNode()
        current_even_node = ListNode()
        while head != None:
            if i % 2 == 0:
                if i == 2:
                    even_head.val = head.val
                    current_even_node = even_head
                else:
                    current_even_node.next = ListNode(head.val, None)
                    current_even_node = current_even_node.next
        
            else:
                if i == 1:
                    odd_head.val = head.val
                    current_odd_node = odd_head
                else:
                    current_odd_node.next = ListNode(head.val, None)
                    current_odd_node = current_odd_node.next
            #print(f"Head: {head}")
            #print(f"Odd Head: {odd_head}")
            #print(f"Even Head:  {even_head}")
            #print(f"i: {i}")
            head = head.next
            i += 1
        if i > 2:
            current_odd_node.next = even_head
        return odd_head
