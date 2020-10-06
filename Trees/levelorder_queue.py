from collections import deque
class Node:
    def __init__(self,key):
        self.key = key 
        self.left = None
        self.right = None
'''
Push the root to the queue ,check the left child and right child
of the node, if not None push them to the queue set the pointer everytime to node which is popped 
and interate as long as the queue becomes empty
'''
def levelorder(root):
    curr = root
    q = deque()

    q.append(curr)
    while q:
        node = q.popleft()
        print(node.key,end = ' ')
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


root = Node(4)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.right = Node(7)
root.right = Node(5)

levelorder(root)