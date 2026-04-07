class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self


class BST:
    def __init__(self, root = None):
        self.root = root
    
    def __str__(self):
        if self.root == None:
            return "NULL "
        else:
            return f"{self.root.key} " + BST(self.root.left).__str__() + BST(self.root.right).__str__()
        
    def min(self, y):
        x = y
        while x != None and x.left != None:
            x = x.left
        return x
    def max(self, y):
        x = y
        while x != None and x.right != None:
            x = x.right
        return x

    def find(self, k):
        return self.find_rec(self.root, k)
    
    def find_rec(self, node, k):
        if node == None or node.key == k:
            return node
        else:
            if node.key > k:
              return  self.find_rec(node.left, k)
            else:
              return  self.find_rec(node.right, k)

    def nxt(self, node):
        if node == None:
            return None
        else:
            if node.right != None:
                return self.min(node.right)
            else:
                y = node.parent
                while y != None and node != y.left:
                    node = y
                    y = node.parent
                return y

    def prv(self, node):
        if node == None:
            return None
        else:
            if node.left != None:
                return self.max(node.left)
            else:
                y = node.parent
                while y != None and node == y.left:
                    node = y
                    y = node.parent
                return y

    def insert(self, node):
        if node == None:
            return None
        else:
            y = None
            x = self.root
            while x != None:
                if x.key > node.key:
                    y = x
                    x = x.left
                else:
                    y = x
                    x = x.right
            if y == None:
                self.root = node
            else:
                node.parent = y
                if y.key > node.key:
                    y.left = node
                else:
                    y.right = node

    def remove(self, node):
        if node == None:
            return None
        else:
            if(node.left == None or node.right == None):
                x = node
            else:
                x = self.nxt(node)
            if(x.left != None):
                v = x.left
            else:
                v = x.right
            if(x.parent == None):
                self.root = v
            else:
                if(x == x.parent.left):
                    x.parent.left = v
                else:
                    x.parent.right = v
            if v is not None:
                v.parent = x.parent
            if(x != node):
                node.key = x.key


    def rotate_right(self, node):
        if node == None or node.left == None:
            return None
        else:
            p = node.parent
            y = node.left
            if(p == None):
                y.parent = None
                self.root = y
            else:
                y.parent = p
                if(node == p.left):
                    p.left = y
                else:
                    p.right = y
            z = y.right
            node.left = z
            if z != None:
                z.parent = node
            y.right = node
            node.parent = y




    def rotate_left(self, node):
        if node == None or node.right == None:
            return None
        else:
            p = node.parent
            y = node.right
            if(p == None):
                y.parent = None
                self.root = y
            else:
                y.parent = p
                if(node == p.left):
                    p.left = y
                else:
                    p.right = y
            z = y.left
            node.right = z
            if z != None:
                z.parent = node
            y.left = node
            node.parent = y
 