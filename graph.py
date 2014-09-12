__author__ = 'federicocastro'

from collections import deque


class Tree(object):

    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r
        self.visited = False

    def __repr__(self):
        return 'T(%s)' % self.x

    def visit(self):
        self.visited = True

    def is_visited(self):
        return self.visited

    def next_child(self):
        if self.l and not self.l.is_visited():
            return self.l
        elif self.r and not self.r.is_visited():
            return self.r


def bfs(tree):
    result = []

    if not tree:
        return result

    queue = deque([tree])
    result.append(tree.x)
    tree.visit()

    while queue:
        t = queue[0]
        next_child = t.next_child()
        if next_child:
            result.append(next_child.x)
            next_child.visit()
            queue.append(next_child)
        else:
            queue.popleft()

    return result


def dfs(tree, return_paths=False):
    result, paths = [], []

    if not tree:
        return (result, paths) if return_paths else result

    stack = [tree]
    result.append(tree.x)
    tree.visit()

    while stack:
        t = stack[-1]
        next_child = t.next_child()
        if next_child:
            result.append(next_child.x)
            next_child.visit()
            stack.append(next_child)
        else:
            if return_paths:
                paths.append([t.x for t in stack])
            stack.pop()

    return (result, paths) if return_paths else result


def get_tree_for_test():
    return[
        None,

        Tree(5,
             l=Tree(3),
             r=Tree(10)),

        Tree(5),

        Tree(5,
             l=Tree(3,
                    l=Tree(20),
                    r=Tree(21,
                           l=Tree(23)
                    )
             ),
             r=Tree(10,
                    l=Tree(1)
             )
        ),

        Tree(5,
             l=Tree(40,
                    l=Tree(3,
                           l=Tree(20),
                           r=Tree(21, l=Tree(23))
                    )),
             r=Tree(10, l=Tree(1))
        ),

        Tree(5, l=Tree(10, l=Tree(1)))
    ]