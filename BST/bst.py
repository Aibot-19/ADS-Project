class TreeNode:         # represents single node in a BST (binary search tree)
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        # updates parent pointers if children are provided
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self


class BST:                  # represents a binary search tree data structure 
    def __init__(self, root = None):
        self.root = root
    
    def __str__(self):          # return string representation of tree
        if self.root == None:
            return "NULL "
        else:
            return f"{self.root.key} " + BST(self.root.left).__str__() + BST(self.root.right).__str__()
        
    def min(self, y):           # finds node with minimum key
        x = y
        while x != None and x.left != None:
            x = x.left
        return x
    def max(self, y):           # finds node with maximum key
        x = y
        while x != None and x.right != None:
            x = x.right
        return x

    def find(self, k):              # searchs key in BST
        return self.find_rec(self.root, k)
    
    def find_rec(self, node, k):            # recursive helper for find function 
        if node == None or node.key == k:
            return node
        else:
            if node.key > k:
              return  self.find_rec(node.left, k)
            else:
              return  self.find_rec(node.right, k)

    def nxt(self, node):               # finds successor of given node
        if node == None:
            return None
        else:
            # Case 1: right subtree isnt' NIL, suc is minimum of that tree
            if node.right != None:
                return self.min(node.right)
            # Case 2: right subtree is NIl, suc is one of the ancestors
            else:
                y = node.parent
                while y != None and node != y.left:
                    node = y
                    y = node.parent
                return y

    def prv(self, node):                # finds predecessor of given node
        if node == None:
            return None
        else:
            # Case 1: left subtree isn't NIL, pred is maximum of that tree
            if node.left != None:
                return self.max(node.left)
            # Case 2: left subtree is NIL, goes up until it finds a node ---> that is predecessor, right child of given node parent
            else:
                y = node.parent
                while y != None and node == y.left:
                    node = y
                    y = node.parent
                return y

    def insert(self, node):             # inserts node into BST maintaining BST property
        if node == None:
            return None
        else:
            y = None                # new node's parent
            x = self.root
            # finds insertion point 
            while x != None:
                if x.key > node.key:
                    y = x
                    x = x.left
                else:
                    y = x
                    x = x.right
            # if tree was empty, new node is root
            if y == None:
                self.root = node
            else:
                node.parent = y
                # attaches new node as left or right child 
                if y.key > node.key:
                    y.left = node
                else:
                    y.right = node

    def remove(self, node):         # removes given node from BST maintaining BST properties
        if node == None:
            return None
        else:
            # determines which node will be removed from the tree
            # if node has 0 or 1 child, node is removed 
            if(node.left == None or node.right == None):
                x = node
            # if node has 2 children, remove its successor and overwrite it with given tree 
            else:
                x = self.nxt(node)
            # v is x's child, which is being removed 
            if(x.left != None):
                v = x.left
            else:
                v = x.right
            # link x's parent to x's child 
            if(x.parent == None):
                self.root = v   # removes root 
            else:
                if(x == x.parent.left):
                    x.parent.left = v
                else:
                    x.parent.right = v
            # updates v pointer 
            if v is not None:
                v.parent = x.parent
            # if successor was removed, copies successor's data into target node 
            if(x != node):
                node.key = x.key


    def rotate_right(self, node):                   # right rotation around given node maintaining BST properties
        if node == None or node.left == None:
            return None
        else:
            p = node.parent
            y = node.left               # y will be subtree's new root
            # 1. links y to node's parent
            if(p == None):
                y.parent = None
                self.root = y
            else:
                y.parent = p
                if(node == p.left):
                    p.left = y
                else:
                    p.right = y
            # 2. transfers y's right subtree to become node's left subtree 
            z = y.right
            node.left = z
            if z != None:
                z.parent = node
            # 3. link node as y's right child 
            y.right = node
            node.parent = y




    def rotate_left(self, node):            # left  rotation around given node maintaining BST properties 
        if node == None or node.right == None:
            return None
        else:
            p = node.parent
            y = node.right          # y will become new root of this subtree 
            # 1. links y to node's parent
            if(p == None):
                y.parent = None
                self.root = y
            else:
                y.parent = p
                if(node == p.left):
                    p.left = y
                else:
                    p.right = y
            # 2. transfers y's left subtree to become node's right subtree 
            z = y.left
            node.right = z
            if z != None:
                z.parent = node
            # 3. links node as y's left child
            y.left = node
            node.parent = y
 