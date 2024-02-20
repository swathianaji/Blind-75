"""
Problem: 206. Reverse Linked List

URL: https://leetcode.com/problems/reverse-linked-list/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

def reverseList(head):
    before = None
    current = head
    while current is not None:
        after = current.next
        current.next = before
        before = current
        current = after 
    return before

# Sample test case
print(reverseList([1,2,3,4,5]))

