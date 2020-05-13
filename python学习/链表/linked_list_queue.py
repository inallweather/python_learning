"""
@version: 1.0
@author: jack-liu
@file: linked_list_queue.py
@time: 2020/5/11 17:25
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    """
    链表对列
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        """
        定义添加操作在尾部
        :param item: 传一个值
        """
        node = Node(item)
        # 如果为空，则添加节点
        if self.is_empty():
            self.head = node
            return
        # 如果对列不为空
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node  # 最后的个节点就要添加的节点
        node.next = None  # 尾节点指向None节点

    def dequeue(self):
        """
        前端出对列
        :return:  最先的哪个值
        """
        if self.is_empty():
            raise Exception('The queue is not empty!')
        cur = self.head
        self.head = self.head.next
        return cur.value


if __name__ == '__main__':
    q = LinkedListQueue()
    # 队列: 100 200 300
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    # 终端1: 100
    print(q.dequeue())
    # 终端2: False
    print(q.is_empty())
