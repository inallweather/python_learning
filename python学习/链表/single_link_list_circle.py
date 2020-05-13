"""
@version: 1.0
@author: jack-liu
@file: single_link_list_circle.py
@time: 2020/5/11 15:08
"""


class Node:
    """定义节点"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    """定义一个循环链表"""

    def __init__(self):
        self.head = None

    @property
    def length(self):
        """返回链表的长度"""
        if self.is_empty():
            return 0

        count = 1
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next

        return count

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """在头部添加一个节点"""
        node = Node(item)
        # 如果链表为空，则直接添加，并把添加后的节点下next指向自己
        if self.is_empty():
            self.head = node
            node.next = self.head
            return

        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        node.next = self.head  # 把添加后的节点指向头节点
        self.head = node  # 当前要添加的节点就是头节点
        cur.next = node  # 把头节点指向下一个节点

    def append(self, item):
        """在尾部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = node
        node.next = self.head

    def travel(self):
        """遍历每一个节点，并打印其值"""
        cur = self.head
        while cur.next != self.head:
            print(cur.value, end=' ')
            cur = cur.next
        print(cur.value)


if __name__ == '__main__':
    s = SingleLinkList()
    s.add(300)
    s.add(200)
    s.add(100)
    s.append(800)
    s.travel()
    print(s.is_empty())
    print(s.length)
