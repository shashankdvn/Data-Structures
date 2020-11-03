class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

'''
we use a stack and push the right node first because we have to pop the left child
first for the preorder
'''    
def preorder(root):
    s = []
    s.append(root)

    while s:
        curr_node = s.pop()
        print(curr_node.key,end = ' ')
        if curr_node.right is not None:
            s.append(curr_node.right)
        if curr_node.left is not None:
            s.append(curr_node.left)

root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 
preorder(root) 
