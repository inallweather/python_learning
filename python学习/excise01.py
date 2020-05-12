"""
@version: 1.0
@author: jack-liu
@file: excise01.py
@time: 2020/5/11 18:06
"""

"""
【1】题目描述
    输入一个链表，按链表值从尾到头的顺序返回一个 ArrayList
 
【2】试题解析
    将链表的每个值取出来然后存放到一个列表 ArrayList 中
  	解题思路1: 将链表中从头节点开始依次取出节点元素，append到array_list中，并进行最终反转
    解题思路2: 将链表中从头节点开始依次取出节点元素，insert到array_list中的第1个位置
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_linked_from_tail_to_head(self, node):
        array_list = []
        while node:
            array_list.insert(0, node.value)
            node = node.next

        return array_list

    def get_linkedlist_from_tail_to_head(self, node):
        array_list = []
        while node:
            array_list.append(node.value)
            node = node.next
        return array_list[::-1]


if __name__ == '__main__':
    s = Solution()
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    print(s.get_linked_from_tail_to_head(head))
    print('*' * 50)
    print(s.get_linkedlist_from_tail_to_head(head))
