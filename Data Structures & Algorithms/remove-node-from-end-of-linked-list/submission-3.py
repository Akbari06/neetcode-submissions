# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        # Store all nodes in a list
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Index of the node to remove
        remove_index = len(nodes) - n

        # Case 1: removing the head
        if remove_index == 0:
            return head.next
        
        prev = nodes[remove_index-1]
        prev.next = prev.next.next if prev.next else None

        return head