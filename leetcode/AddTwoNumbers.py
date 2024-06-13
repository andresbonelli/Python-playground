from decorators.Decorators import leetcode_test
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@leetcode_test
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    temp_node = ListNode(0)
    result = temp_node
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        summ = x + y + carry
        carry = int(summ / 10)  # rounds remainder to 0 or 1

        result.next = ListNode(summ % 10)
        result = result.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return temp_node.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


addTwoNumbers(l1, l2)
