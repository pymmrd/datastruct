#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    """docstring for Node"""
    def __init__(self, v=None, left=None, right=None, parent=None):
        self.value = v
        self.left = left
        self.right = right
        self.parent = parent


class BTree(object):
    """docstring for BtTee """
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node):
        n = self.root
        if n is None:
            self.root = node
            return

        while True:
            if node.value <= n.value:
                if n.left is None:
                    node.parent = n
                    n.left = node
                    break
                else:
                    n = n.left
            if node.value > n.value:
                if n.right is None:
                    n.parent = n
                    n.right = node
                    break
                else:
                    n = n.right

    def find(self, v):
        n = self.root  # http://yige.org
        while True:
            if n is None:
                return None
            if v == n.value:
                return n
            if v < n.value:
                n = n.left
                continue
            if v > n.value:
                n = n.right

    def find_successor(self, node):
        '''查找后继结点'''
        assert node is None and node.right is not None
        n = node.right
        while n.left is not None:
            n = n.left
        return n

    def delete(self, v):
        n = self.find(v)
        print "delete:", n.value
        del_parent = n.parent
        if del_parent is None:
            self.root = None
            return
        if n is not None:
            if n.left is not None and n.right is not None:
                succ_node = self.find_successor(n)
                parent = succ_node.parent
                if succ_node == parent.left:
                    #if succ_node is left sub tree
                    parent.left = None
                if succ_node == parent.right:
                    #if succ_node is right sub tree
                    parent.right = None
                if del_parent.left == n:
                    del_parent.left = succ_node
                if del_parent.right == n:
                    del_parent.right = succ_node
                succ_node.parent = n.parent
                succ_node.left = n.left
                succ_node.right = n.right
                del n
            elif n.left is not None or n.right is not None:
                if n.left is not None:
                    node = n.left
                else:
                    node = n.right
                node.parent = n.parent
                if del_parent.left == n:
                    del_parent.left = node
                if del_parent.right == n:
                    del_parent.right = node
                del n
            else:
                if del_parent.left == n:
                    del_parent.left = None
                if del_parent.right == n:
                    del_parent.right = None

    def tranverse(self):
        def pnode(node):
            if node is None:
                return
            if node.left is not None:
                pnode(node.left)
            print node.value
            if node.right is not None:
                pnode(node.right)
        pnode(self.root)


def getopts():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option(
        "-i",
        "--input",
        dest="input",
        help=u"help name",
        metavar="INPUT"
    )
    (options, args) = parser.parse_args()
     #print options.input
    return (options.input)

if __name__ == '__main__':
    al = [23, 45, 67, 12, 78, 90, 11, 33, 55, 66, 89, 88, 5, 6, 7, 8, 9, 0, 1, 2, 678]
    bt = BTree()
    for x in al:
        bt.insert(Node(x))
    bt.delete(12)
    bt.tranverse()
    n = bt.find(12)
    if n is not None:
        print "find valud:", n.value
