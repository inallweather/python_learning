"""
@version: 1.0
@author: jack-liu
@file: queue.py
@time: 2020/5/11 17:20
"""


class Queue:
    """
    队列的特点是先进先出（FIFO）
    也可以说从后端进行，前端出
    """

    def __init__(self):
        self.queues = []

    def is_empty(self):
        return self.queues == []

    def push(self, item):
        self.queues.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('The queue is not empty!')
        return self.queues.pop(0)


if __name__ == '__main__':
    q = Queue()
    # 队列: 100 200 300
    q.push(100)
    q.push(200)
    q.push(300)
    # 终端1: 100
    print(q.pop())
    # 终端2: False
    print(q.is_empty())
