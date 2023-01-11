class Student :
    def __init__(self,name,id):
        self.id = id
        self.name = name
        self.left = None
        self.right = None
    def inorder(root):
        if root is not None:
        # Traverse left
            inorder(root.left)

        # Traverse root
            print(str(root.key) + "->", end=' ')

        # Traverse right
            inorder(root.right)
    def isEmpty(root):
        if root is None:
            return True
    def makeEmpty(root):
        if root is None:
            return 
        makeEmpty(root.left)
        makeEmpty(root.right)
        del root
        root == None
        return 
    def insert(root,name,sbd):
        if root is None:
            return Student(name,sbd)
        elif sbd < root.id :
            insert(sbd,root.left)
        elif sbd > root.id :
            insert(sbd,root.right)
        return root
    def search(sbd,root):
        if root is None:
            return None
        if sbd<root.id:
            return search(sbd,root.left)
        elif sbd>root.id:
            return search(sbd,root.right)
        else:
            return root


if __name__ == '__main__':
    root = Student()
    root.insert(root,"Minh",1)
    root.insert(root,"Nam",2)
    root.insert(root,"Luan",3)
    n1 = root.search(1)
    n2 = root.search(4)
    if n1 is not None:
        print("sinh vien thu 1 la :"+ root.name)
    if n2 is None:
        print("khong tim thay sinh vien") 
    root.makeEmpty()
    root.isEmpty()
    print("cay da bi xoa rong")
    
    


