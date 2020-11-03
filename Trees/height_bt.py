from collections import deque

'''
Write a program to calculate the hight of the tree

'''

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    
def height(root):
    q = deque()
    q.append(root)
    res = []
    height =0
    while q:
        curr_level,size = [],len(q)
        
        for _ in range(size):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            curr_level.append(curr.key)
        
        height+=1
        res.append(curr_level)

    return height,res

root = Node(4)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.right = Node(7)
root.right = Node(5)

print(height(root))