"""
Problem: 21. Merge Two Sorted Lists

URL: https://leetcode.com/problems/merge-two-sorted-lists/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# while both lists are present, only then we can compare, create node and assign whichever value is small
# if one is longer than others add remaining node to new linkedlist


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        temp = None
        while list1 and list2:
            newNode = ListNode()
            if list1.val <= list2.val:
                newNode.val = list1.val
                list1 = list1.next
            elif list2.val < list1.val:
                newNode.val = list2.val
                list2 = list2.next
            if res is None:
                res = newNode
                temp = newNode
            else:
                temp.next = newNode
                temp = temp.next
        while list1:
            newNode = ListNode()
            newNode.val = list1.val
            list1 = list1.next
            if res is None:
                res = newNode
                temp = newNode
            else:
                temp.next = newNode
                temp = temp.next
        while list2:
            newNode = ListNode()
            newNode.val = list2.val
            list2 = list2.next
            if res is None:
                res = newNode
                temp = newNode
            else:
                temp.next = newNode
                temp = temp.next
        return res