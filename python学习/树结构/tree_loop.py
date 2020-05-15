"""
@version: 1.0
@author: jack-liu
@file: tree_loop.py
@time: 2020/5/13 11:46
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    """
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印， 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推
    """
    def print_tree_one_to_more(self, root):
        if root is None:
            return
        cur_q = [root]
        next_q = []
        level = 1
        while cur_q:
            cur = cur_q.pop(0)
            print(cur.value, end=' ')
            if cur.left:
                next_q.append(cur.left)
            if cur.right:
                next_q.append(cur.right)
            if not cur_q:
                cur_q, next_q = next_q, cur_q
                level += 1
                print()


if __name__ == '__main__':
    s = Solution()
