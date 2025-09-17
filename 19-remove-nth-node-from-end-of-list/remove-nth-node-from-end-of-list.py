# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Brute Force Approach

        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next

        # removeIndex = len(nodes) - n
        # if removeIndex == 0:
        #     return head.next

        # nodes[removeIndex - 1].next = nodes[removeIndex].next
        # return head

        # Iteration

        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next

        removeIndex = N - n
        if removeIndex == 0:
            return head.next

        cur = head
        for i in range(N - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head