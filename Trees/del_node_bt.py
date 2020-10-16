from collections import deque
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


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
            curr = node.right
        else:
            return


def del_last_node(root,d_node):
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        if curr.left:
            if curr.left is d_node:
                curr.left = None
                return
            else:
                q.append(curr.left)
        if curr.right:
            if curr.right is d_node:
                curr.right = None
                return
            else:
                q.append(curr.right)

def del_node(root,key):
    q  = deque()
    key_node = None
    q.append(root)

    while q:
        curr  = q.popleft()
        if curr.key == key:
            key_node = curr

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    if key_node:
        x = curr.key
        del_last_node(root,curr)
        key_node.key = x





            




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
    print("The tree before the deletion:") 
    inorder(root) 
    key = 7
    del_node(root, key) 
    print() 
    print("The tree after the deletion;") 
    inorder(root) 