class Node:
    def __init__(self,key):
        self.key =key
        self.left = None
        self.right = None


if __name__ == "__main__":
    root= Node(3)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right= Node(6)
    root.right.right = Node(7)
    
