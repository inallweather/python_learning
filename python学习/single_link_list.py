"""
@version: 1.0
@author: jack-liu
@file: single_link_list.py
@time: 2020/5/11 14:16
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    def __init__(self):
        self.head = None

    @property
    def size(self):
        """输入链表的大小"""
        count = 0
        while self.head:
            count += 1
            self.head = self.head.next
        return count

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def add(self, item):
        """在头部添加一项数据"""
        node = Node(item)

        node.next = self.head
        self.head = node

    def append(self, item):
        """在其尾部添加数据"""
        node = Node(item)
        cur = self.head
        # 如果为空，则直接添加
        if self.is_empty():
            cur = node
            return
            # 如果不不空：则需要遍历的最后一个节点，然后修改最后一个节点的next指向None
        while cur.next:
            cur = cur.next
        cur.next = node  # 把最后一个节点的next指向添加的值
        node.next = None  # 在添加的的节点的next指向空

    def travel(self):
        """遍历并打印每一项"""
        cur = self.head
        while cur:
            print(cur.value, end=' ')
            cur = cur.next
        print()


if __name__ == '__main__':
    s = SingleLinkList()
    s.add(100)
    s.add(300)
    s.append(500)
    s.add(800)
    s.travel()
    print(s.is_empty())
    print(s.size)
