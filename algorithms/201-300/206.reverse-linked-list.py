# 反转链表
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # dummy = ListNode(float('-inf'))

        # while head:
        #     dummy.next, head.next, head = head, dummy.next, head.next

        # return dummy.next

        # # 第二种解法 使用递归的方法
        # if head == None or head.next == None:
        #     return head
        # node = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return node

        # 采用迭代方式
        if head is None or head.next is None:
            return head
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)


print(Solution().reverseList(l))
