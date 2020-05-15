"""
@version: 1.0
@author: jack-liu
@file: linked_del_repeat.py
@time: 2020/5/13 10:26
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def del_linked_repeat_item(self, head):
        if head is None:
            return head
        cur = head
        while cur.next:
            if cur.value == cur.next.value:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == '__main__':
    s = Solution()
    head = Node(100)
    p1 = Node(200)
    p2 = Node(200)
    p3 = Node(200)
    p4 = Node(400)
    p5 = Node(500)
    head.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    p = s.del_linked_repeat_item(head)
    while p:
        print(p.value, end=' ')
        p = p.next
