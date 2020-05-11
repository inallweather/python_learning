"""
@version: 1.0
@author: jack-liu
@file: link_stack.py
@time: 2020/5/11 16:54
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkStack:
    """
    链表栈实现
     先进后出，FILO，只能操作一端
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        """在头部添加"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.is_empty():
            raise Exception('The stack is not emtpy')
        value = self.head.value
        self.head = self.head.next
        return value


if __name__ == '__main__':
    s = LinkStack()
    # 栈（栈底->栈顶）：300 200 100
    s.push(100)
    s.push(200)
    s.push(300)
    # 终端1: 300
    print(s.pop())
    # 终端2: False
    print(s.is_empty())








