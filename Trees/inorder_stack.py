'''
Program for the Inorder traversal of a binary tree
without recursion using stack(list)
'''
class Node:
    def __init__(Self,key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    current = root
    s = []
    while True:
        if current is not None:
            s.append(current)
            current = current.left
        elif s:
            current = s.pop()
            print(current.key,end = ' ')
            current = current.right
        else:
            break

""" Constructed binary tree is 
            5
          /   \ 
         6     3             
       /  \    /
      4    5  2   """
  
root = Node(5) 
root.left = Node(2) 
root.right = Node(3)
root.left = Node(2) 
root.left.left = Node(4) 
root.left.right = Node(5) 

inorder(root)