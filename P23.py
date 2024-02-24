"""
Problem: 141. Linked List Cycle

URL: https://leetcode.com/problems/linked-list-cycle/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# When you use slow and fast pointer, those two will become equal at some point if linked list is a cycle

def hasCycle(self, head) -> bool:
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False