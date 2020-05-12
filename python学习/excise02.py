"""
@version: 1.0
@author: jack-liu
@file: excise02.py
@time: 2020/5/11 18:06
"""

"""
【【1】题目描述
    输入一个链表，输出该链表中倒数第 k 个节点
  
【2】试题解析
    可将链表中的每一个元素保存到列表中，在列表中寻找倒数第 k 个元素
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    def find_k_tail(self, node, k):
        k_list = []
        while node:
            k_list.append(node.value)
            node = node.next
        if k > len(k_list) or k < 1:
            return None
        return k_list[-k]


if __name__ == '__main__':
    s = Solution()
    # 100 200 300, 500
    n1 = Node(100)
    n1.next = Node(200)
    n1.next.next = Node(300)
    n1.next.next.next = Node(500)
    # 倒数第2个：300
    result = s.find_k_tail(n1, 2)
    print(result)
