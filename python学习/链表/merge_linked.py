"""
@version: 1.0
@author: jack-liu
@file: merge_linked.py
@time: 2020/5/12 13:52
题目：
    输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MergeLinkedList:
    """
    合并两个增量链表，并生成一个新的满足单调不减规则并返回
    """

    def merge_two_linked_one(self, head, head1):
        h1 = head
        h2 = head1
        # 先判断两个链表不为空的情况，新生成的链表头
        if h1 and h2:
            if h1.value > h2.value:  # 找到小的哪个为链表头
                new_linked = h2
                h2 = h2.next
            else:
                new_linked = h1
                h1 = h1.next
            merge_linked = new_linked  # 返回合并后的链表表头
        elif h1:  # 如果h1不为空，则直接返回h1
            return h1
        else:  # 如果h2不为空或着都是空，则直接返回h2，h2或是h2，或是None
            return h2
        # 遍历两个链表,如果两个链表都不为空的情况下：
        # 找到两两比较其中小的哪作为下一个节点，并移动两游标
        # 然后移到两个链表，同时也需要把新生成合并的链表的游标也进行移动
        while h1 and h2:
            if h1.value <= h2.value:
                new_linked.next = h1
                h1 = h1.next
            else:
                new_linked.next = h2
                h2 = h2.next
            new_linked = new_linked.next
        if h2:
            new_linked.next = h2
        elif h1:
            new_linked.next = h1

        return merge_linked


if __name__ == '__main__':
    s = MergeLinkedList()
    # 链表1： 100->200->300->400->None
    head1 = Node(100)
    head1.next = Node(200)
    head1.next.next = Node(300)
    head1.next.next.next = Node(400)
    # 链表2：1->200->600->None
    head2 = Node(1)
    head2.next = Node(200)
    head2.next.next = Node(600)
    # 测试方法
    p = s.merge_two_linked_one(head1, head2)
    while p:
        print(p.value, end=" ")
        p = p.next
