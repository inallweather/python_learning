"""
@version: 1.0
@author: jack-liu
@file: two_stack_queue.py
@time: 2020/5/11 17:54
"""


class TwoStackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()


if __name__ == '__main__':
    s = TwoStackQueue()
    # 入栈: 100 200 300
    s.push(100)
    s.push(200)
    s.push(300)
    # 终端1: 100
    print(s.pop())
    print(s.pop())
    print(s.pop())
