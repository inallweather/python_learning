"""
@version: 1.0
@author: jack-liu
@file: stack.py
@time: 2020/5/11 16:19
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('please check the stack,is it a empty?')
        return self.stack.pop()


if __name__ == '__main__':
    s = Stack()
    # 栈(栈底->栈顶): 100 200 300
    s.push(100)
    s.push(200)
    s.push(300)
    # 终端1: 300 200 100 异常
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
