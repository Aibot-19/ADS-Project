from BST import BST 

class AVL(BST):
    def __init__(self, root = None):
        super().__init__(root)

    def _get_height(self, node):           # restituisce altezza nodo altrimenti none
        if node is None:
            return 0
        return getattr(node, 'height', 0)           # prende attributo altezza anche da nodi appena creati
    
    def _update_node_height(self, node):        # applica formula 1 + max(h(left), h(right)), chiamata dopo insert o del
        if node is not None:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    

    def _rebalance(self, x):               # risale a nodo x verso la radice correggendo sbilanciamenti delle altezze
        while x is not None:
            self._update_node_height(x)
            h_left = self._get_height(x.left)
            h_right = self._get_height(x.right)
                                # sbilanciamento a sx
            if h_left - h_right > 1:
                y = x.left
                if self._get_height(y.left) < self._get_height(y.right):
                    self.rotate_left(y)
                    self._update_node_height(y)
                    self._update_node_height(x.left)                    # y diventa nipote o figlio
                                 # rotazione destra su nodo sbilanciato
                self.rotate_right(x)
                self._update_node_height(x)
                self._update_node_height(x.parent)
                x = x.parent                                            # dopo rotazione, genitore bilanciato
                                # sbilanciamento a dx
            elif h_right - h_left > 1:
                y = x.right
                if self._get_height(y.right) < self._get_height(y.left):
                    self.rotate_right(y)
                    self._update_node_height(y)
                    self._update_node_height(x.right)
                                  # rotazione sx su nodo bilanciato
                self.rotate_left(x)
                self._update_node_height(x)
                self._update_node_height(x.parent)
                x = x.parent
            x = x.parent


    def insert(self, node):                 # inserimento AVL: inserimento BST + ribilanciamento
        node.height = 1
        super().insert(node) 
        self._rebalance(node.parent)                               # ribilancia partendo dal nodo padre 
                                                                     # (nodo appena inserito non può essere sbilanciato, è foglia)


    def remove(self, node):                 # rimozione AVL: rimozione BST + ribilanciamento
        if node.left and node.right:                    # 2 figli, rimuove successore
            y = self.nxt(node)
            start_node = y.parent
            if start_node == node:                      # successore=figlio, start deve rimanere suc
                start_node = node
        else:
            start_node = node.parent
        super().remove(node)                        # rimozione standard
        self._rebalance(start_node)


