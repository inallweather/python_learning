"""
@version: 1.0
@author: jack-liu
@file: linked_public_node.py
@time: 2020/5/12 11:29
题目：
    输入两个链表，找出它们的第一个公共节点
"""
import math


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def _get_list(self, head):
        cur = head
        li = []
        while cur:
            li.append(cur)
            cur = cur.next
        return li

    def get_linked_public_node(self, head, head1):
        li1 = self._get_list(head)
        li2 = self._get_list(head1)
        print(id(li1[-1]))
        print(id(li2[-1]))
        node = None
        # 判断两个列表是否不为空，及两个列表的最后一是否相等，如果不为空，且两个对象相等，则弹出两个列表中的最后一项，并保存其弹出项
        # 如果两个对象不相等，那么前一个相等的对象就是其中要找的公共节点，并返回
        while li1 and li2 and li1[-1] is li2[-1]:
            node = li1.pop()
            li2.pop()
        return node


if __name__ == '__main__':
    s = Solution()
    n100 = Node(100)
    n200 = Node(200)
    n300 = Node(300)
    n400 = Node(400)
    n666 = Node(666)
    n888 = Node(888)
    # 链表1：100 -> 200 -> 300 -> 400 -> None
    head1 = n100
    head1.next = n200
    n200.next = n300
    n300.next = n400
    # 链表2：666 -> 888 -> 300 -> 400 -> None
    head2 = n666
    head2.next = n888
    n888.next = n300
    n300.next = n400

    print(s.get_linked_public_node(head1, head2).value)
