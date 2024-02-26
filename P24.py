"""
Problem: Merge K Sorted Lists

URL: https://leetcode.com/problems/merge-k-sorted-lists/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        res = None
        temp = None

        while lists:
            minValue = 10**4+1
            minIndex = -1
            for i in range(len(lists)):
                if lists[i] and minValue > lists[i].val:
                    minValue = lists[i].val
                    minIndex = i
            if minIndex == -1:
                break
            newNode = ListNode()
            newNode.val = minValue
            if not res:
                res = newNode
                temp = newNode
            else:
                temp.next = newNode
                temp = temp.next
            lists[minIndex] = lists[minIndex].next
            if not lists[minIndex]:
                lists.pop(minIndex)
        return res

        