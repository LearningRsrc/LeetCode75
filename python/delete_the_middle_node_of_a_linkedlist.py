# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        copy_head = head
        while copy_head.next != None:
            n += 1
            copy_head = copy_head.next
        index = n // 2
        
        i = 0
        new_head = ListNode(head.val)
        if index  == 0:
            new_head = None
            return new_head
        current_node = new_head
        #print(f"Input head: {head}")
        #print(f"n: {n}")
        #print(f"index: {index}")
        while head != None:
            #print(f"i: {i}")
            if i == index:
                i += 1
                head = head.next
                continue
            else:
                #print(f"head: {head.val}")
                new_node = ListNode(head.val)
                #print(f"new head: {new_head}")
                if i == 0:
                    #new_head.next = new_node
                    current_node = new_head
                else:
                    #print()
                    current_node.next = new_node
                    current_node = new_node
            #if i + 1 == n:
            #    return new_head
            i += 1
            head = head.next
        return new_head
