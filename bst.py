class hashNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.value = value
        self.key = key
    
class node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
class BST:
    def __init__(self):
        self.root = None
    
    def search(root, key):
        if root is None:
            return root
        if root.key==key:
            return root.value
        elif (root.key>key):
            return search(root.left, key)
        return search(root.right, key)
    
    def minvalue(root):
        while root.left != None:
            root = root.left
        return root
    
    def put(root, key, value):
        new_node = hashNode(key, value)
        if root is None:
            root = new_node
        if root.key<key:
            if root.right == None:
                root.right = new_node
            else:
                put(root.right, key, value)
        else:
            if root.left == None:
                root.left = new_node
            else:
                put(root.left, key, value)
        
    def delete(root, key):
        if root is None:
            return None
        if key<root.key:
            root.left = delete(root.left, key)
        elif key>root.key:
            root.right = delete(root.right, key)
        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            
            temp = minvalue(root.right)
            root.key = temp.key
            root.right = delete(root.key, temp.key)
            
        return root
    
    def preorder(root):
        if root is None:
            return
        print(root.key+"   "+root.value)
        preorder(root.left)
        preorder(root.right)
    
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        print(root.key+"   "+root.value)
        inorder(root.right)
    
    def postorder(root):
        if root is None:
            return
        postorder(root.left)
        postorder(root.right)
        print(root.key+"   "+root.value)
    
    