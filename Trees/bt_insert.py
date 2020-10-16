'''
Write a program to insert and element in the missing part
of the level order
'''

from collections import deque
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def insert(root,key):
    q = deque()

    q.append(root)

    while q :
        curr =q.popleft()
        if not curr.left:
            curr.left = Node(key)
            return
        else:
            q.append(curr.left)
        if not curr.right:
            curr.right = Node(key)
            return
        else:
            q.append(curr.right)

def inorder(root):
    curr = root
    s = []
    while True:
        while curr:
            s.append(curr)
            curr = curr.left
        if s:
            node = s.pop()
            print(node.key,end = ' ')
            curr= node.right
        else:
            return



if __name__ == '__main__':
    '''
         4
        / \
       3   5
      / \
     2   1
          \
           7
     '''
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.right = Node(7)
    root.right = Node(5)

    print("Before Insertion level order traversal:",end='\n')
    inorder(root)
    insert(root,6)
    print("After Insertion level order traversal:")
    inorder(root)


    # insert()
