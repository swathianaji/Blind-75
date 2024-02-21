"""
Problem: 143. Reorder List

URL: https://leetcode.com/problems/reorder-list/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""
# we can use stack to get node from the beginning
# queue to get nodes from end

def reorderList(self, head: Optional[ListNode]) -> None:
    queue = []
    stack = []
    count = 0
    while head:
        queue.append(head)
        stack.append(head)
        count += 1
        head = head.next
    head = queue[0]
    count -= 1
    q = 1
    s = -1
    temp = head
    while count:
        temp.next = stack[s]
        temp =  temp.next
        count -= 1
        s -= 1
        if count == 0:
            break
        temp.next = queue[q]
        temp = temp.next
        count -= 1
        q += 1
    temp.next = None
    return head        