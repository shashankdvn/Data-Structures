"""
Write a program to check whether the Trees are identical
"""

from collections import deque
class Node:
    def __init__(self,key):
        self.key  = key
        self.left = None
        self.right =None


def checktree(x,y):
    q = deque()
    q.append((x,y))
    while q:
        n1,n2 = q.popleft()
        if not n1 and not n2:
            continue
        elif None in [n1,n2]:
            return False
        else:
            if n1.key != n2.key:
                return False
            q.append((n1.left,n2.left))
            q.append((n1.right,n2.right))
    return True

root = Node(4)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.right = Node(7)
root.right = Node(5)

root1 = Node(4)
root1.left = Node(3)
root1.left.left = Node(2)
root1.left.right = Node(1)
root1.left.right.right = Node(7)
root1.right = Node(5)
import pdb;pdb.set_trace()
print(checktree(root,root1))