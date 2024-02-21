"""
Problem: 19. Remove Nth Node From End of List

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Count number of nodes
# Skip Node when new_count == count-n

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        temp = head
        new_count = 0
        if n == count:
            return head.next
        while True:
            new_count += 1
            if new_count == count - n:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head