# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute Force Approach

        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None
        
        
        
        # Slow and Fast Pointer

        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # second = slow.next
        # prev = slow.next = None
        # while second:
        #     temp = second.next
        #     second.next = prev
        #     prev = second
        #     second = temp
        
        # first, second = head, prev
        # while second: 
        #     temp1, temp2 = first.next, second.next
        #     first.next = second
        #     second.next = temp1
        #     first, second = temp1, temp2

        