"""
@version: 1.0
@author: jack-liu
@file: linked_reverse.py
@time: 2020/5/12 10:27
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedListReverse:
    """
    传入一个链表，反转链表后，并返回第一节点
    """

    def get_linked_reverse(self, head):
        """
        传入一个链表，反转链表后并发反转的首节点
        :param head:  链表
        :return: 反转后的链表头节点
        """
        if head is None:
            return head

        pre = None
        cur = head
        while cur:
            next_node = cur.next  # 先把当前游标的第下一个节点保存起来
            cur.next = pre  # 把当前的节点指向前一个节点（用于反转）
            pre = cur  # 把前一个节点移动到当前节点上
            cur = next_node  # 把当前节点下移一个
        return pre


if __name__ == '__main__':
    s = LinkedListReverse()
    node = Node(100)
    node.next = Node(200)
    node.next.next = Node(300)
    node.next.next.next = Node(500)
    print(s.get_linked_reverse(node))
