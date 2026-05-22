from BST import BST, TreeNode

def color(node):
    return getattr(node, "color", "black") if node != None else "black" 

class RBTree(BST):
    def __init__(self, root=None):
        super().__init__(root)

    def _get_color(self, node):                 # returns color node, if node=None
        if node is None:
            return "black"
        return getattr(node, 'color', "black")
    
    def _set_color(self, node, color_string):          # assigns color to node if it exists
        if node is not None:
            node.color = color_string


    def insert(self, node):
        self._set_color(node, "red")                # new nodes = red
        super().insert(node)
        self._fix_insert(node)

    def _fix_insert(self, z):                   # fixes errors after insertion
        while z.parent and self._get_color(z.parent) == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right           # y = uncle
                # Case 1: uncle is red
                if self._get_color(y) == "red":
                    self._set_color(z.parent, "black")
                    self._set_color(y, "black")
                    self._set_color(z.parent.parent, "red")
                    z = z.parent.parent
                # Case 2: uncle is black, z is uncle's right child
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)
                # Case 3: uncle is black, z is uncle's left child
                    self._set_color(z.parent, "black")
                    self._set_color(z.parent.parent, "red")
                    self.rotate_right(z.parent.parent)
                # Case 4: symmetrical, z.parent is right child
            else:
                y = z.parent.parent.left      # symmetrical cases
                if self._get_color(y) == "red":
                    self._set_color(z.parent, "black")
                    self._set_color(y, "black")
                    self._set_color(z.parent.parent, "red")
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(z)
                    self._set_color(z.parent, "black")
                    self._set_color(z.parent.parent, "red")
                    self.rotate_left(z.parent.parent)                
        self._set_color(self.root, "black")


    def _rb_switch(self, u, v):                     # u is node to remove, v is the node to put in its place
    # helps the remove function when it needs to swap node with his successor after removal
        # Case 1: u root of subtree, v becomes new root
        if u.parent is None:
            self.root = v
        # Case 2: u is left child, v is connected to left side of parent
        elif u == u.parent.left:
            u.parent.left = v
        # Case 3:u is right child, v is connected to right side of parent
        else:
            u.parent.right = v
        # if v is not a NIL node, update pointer to father if v != NIL, pointer to father is updated
        if v is not None:
            v.parent = u.parent


    def remove(self, node):                     # removes node from tree switching pointers, if the node was black height needs to be fixed
        y = node
        y_original_color = self._get_color(y)
        # Case 1: left child of node to remove is NIL
        if node.left is None:
            x = node.right                              # x is node who takes y place, if it's NIL we use his parent
            p = node.parent
            self._rb_switch(node, node.right)           # swapping using previous function 
        # Case 2: right child of node to remove is NIL
        elif node.right is None:
            x = node.left
            p = node.parent
            self._rb_switch(node, node.left)
        # Case 3: node to remove has both children, we use successor
        else:
            y = self.nxt(node)              # find successor and memorize its color 
            y_original_color = self._get_color(y)
            x = y.right                                              # successor is always without left child, his right child takes place of successor
            if y.parent == node:                # if successor is right child of node to remove 
                p = y                               # y will be the new parent 
                if x: x.parent = y                  # fixing pointers
            else:                              # if successor is deeper 
                p = y.parent                        
                self._rb_switch(y, y.right)         # swap y and its child
                y.right = node.right                # y is new root of right subtree
                y.right.parent = y                  # updating pointer
                                               # neither of previous cases
            self._rb_switch(node, y)                # substitution of node with y's successor
            y.left = node.left                      # y root of left subtree
            y.left.parent = y
            self._set_color(y, self._get_color(node))   
        
        # rebalance tree if black node was removed
        if y_original_color == "black":
            self._fix_remove(x, p)

    def _fix_remove(self, x, p):                # restores tree properties if black node was removed, x is new node and p is x.parent 
        while x != self.root and self._get_color(x) == "black":
            # x is left child of p
            if x == p.left:              
                w = p.right              # sibling of w
                # Case 1: red sibling
                if self._get_color(w) == "red":             # paints sibling black and parent red, left rotate to arrive in another case
                    self._set_color(w, "black")
                    self._set_color(p, "red")
                    self.rotate_left(p)
                    w = p.right
                # Case 2: black sibling with black children 
                if self._get_color(w.left) == "black" and self._get_color(w.right) == "black":          # paints sibling red and goes back to root 
                    self._set_color(w, "red")
                    x = p
                    p = x.parent if x else None
                # Case 3: black sibling with right child black and left child red
                else:                               # paints sibling red and both children black, right rotate to arrive in case 4
                    if self._get_color(w.right) == "black":
                        self._set_color(w.left, "black")
                        self._set_color(w, "red")
                        self.rotate_right(w)
                        w = p.right
                # Case 4: black sibling, right child red and left child black
                    self._set_color(w, self._get_color(p))
                    self._set_color(p, "black")
                    self._set_color(w.right, "black")
                    self.rotate_left(p)
                    x = self.root
            # x is black child of p, symmetrical case 
            else:
                w = p.left          # sibling
                # same cases but symmetrical  
                if self._get_color(w) == "red":
                    self._set_color(w, "black")
                    self._set_color(p, "red")
                    self.rotate_right(p)
                    w = p.left
                
                if self._get_color(w.right) == "black" and self._get_color(w.left) == "black":
                    self._set_color(w, "red")
                    x = p
                    p = x.parent if x else None
                else:
                    if self._get_color(w.left) == "black":
                        self._set_color(w.right, "black")
                        self._set_color(w, "red")
                        self.rotate_left(w)
                        w = p.left
                    
                    self._set_color(w, self._get_color(p))
                    self._set_color(p, "black")
                    self._set_color(w.left, "black")
                    self.rotate_right(p)
                    x = self.root
        # x node (or root) becomes black to balance black height 
        self._set_color(x, "black")


