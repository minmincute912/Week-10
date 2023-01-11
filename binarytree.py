class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right= None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+'->'+" ")
        inorder(root.right)
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def insertleft(node,key):
    if node == None:
        return None
    if (node.left):
        return insertleft(node.left,key)
    else:
        node.left = Node(key)
        return node.left
def insertright(node,key):
    if node == None:
        return None
    if (node.right):
        return insertleft(node.right,key)
    else:
        node.right = Node(key)
        return node.right
def search(root,key):
    if root is None:
        if root.key == key:
            print()
        search(root.left,key)
        search(root.right,key)
    else:
        return root
def deleteleft(root):
    if root == None:
        return None
    if root.left == None:
        return None
    root.left = deleteleft(root.left)
def deleteright(root):
    if root == None:
        return None
    if root.right == None:
        return None
    root.right = deleteright(root.right)
        
    
def size(root):
        if root is None:
            return 0
        else:
            return size(root.left)+ 1+ size(root.right)
