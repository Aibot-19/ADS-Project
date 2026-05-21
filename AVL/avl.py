from BST import BST 

class AVL(BST):
    def __init__(self, root = None):
        super().__init__(root)

    def _get_height(self, node):           # returns node height otherwise none
        if node is None:
            return 0
        return getattr(node, 'height', 0)           # takes height attribute even from newly created nodes
    
    def _update_node_height(self, node):        # applies formula 1 + max(h(left), h(right)), called after insert or delete
        if node is not None:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    

    def _rebalance(self, x):               # goes back from node x towards the root correcting height imbalances
        while x is not None:
            self._update_node_height(x)
            h_left = self._get_height(x.left)
            h_right = self._get_height(x.right)
                                # unbalanced on the left 
            if h_left - h_right > 1:
                y = x.left
                if self._get_height(y.left) < self._get_height(y.right):
                    self.rotate_left(y)
                    self._update_node_height(y)
                    self._update_node_height(x.left)                    # y becomes nephew or child
                                 # right rotation on unbalanced node
                self.rotate_right(x)
                self._update_node_height(x)
                self._update_node_height(x.parent)
                x = x.parent                                            # after rotation parent is balanced
                                # unbalanced on the right
            elif h_right - h_left > 1:
                y = x.right
                if self._get_height(y.right) < self._get_height(y.left):
                    self.rotate_right(y)
                    self._update_node_height(y)
                    self._update_node_height(x.right)
                                  # left rotate on balanced node
                self.rotate_left(x)
                self._update_node_height(x)
                self._update_node_height(x.parent)
                x = x.parent
            x = x.parent


    def insert(self, node):                 # AVL insert: BST insert + rebalancing
        node.height = 1
        super().insert(node) 
        self._rebalance(node.parent)                               # rebalances starting from parent node 
                                                                     # newly inserted node can't be unbalanced, it's a leaf!


    def remove(self, node):                 # AVL delete: BST delete + rebalancing
        if node.left and node.right:                    # if there are 2 child, removes successor
            y = self.nxt(node)
            start_node = y.parent
            if start_node == node:                      # successor = child, start remains on successor
                start_node = node
        else:
            start_node = node.parent
        super().remove(node)                        # removes standard
        self._rebalance(start_node)


