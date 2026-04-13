from BST import BST, TreeNode

class RB_Node(TreeNode):
    def __init__(self, key, color=1):           # poniamo nodi nuovi come rossi
        super().__init__(key)
        self.color = color                          # 1 = rosso, 0 = nero


class RBT(BST):
    def __init__(self):
        super().__init__()
        self.RED = 1
        self.BLACK = 0

    def _get_color(self, node):                 # restituisce colore nodo, se è None (NIL) è nero
        if node is None:
            return self.BLACK
        return getattr(node, 'color', self.BLACK)
    
    def _set_color(self, node, color):          # assegna colore a nodo, se esiste
        if node is not None:
            node.color = color


    def insert(self, node):
        node.color = self.RED                   # i nuovi nodi sono rossi
        super().insert(node)
        self._fix_insert(node)

    def _fix_insert(self, z):                   # risolve gli errori post inserimento
        while z.parent and z.parent.color == self.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right           # è lo zio
                # Caso 1: zio rosso
                if y and y.color == self.RED:
                    z.parent.color = self.BLACK
                    y.color = self.BLACK
                    z.parent.parent.color = self.RED
                    z = z.parent.parent
                # Caso 2: zio nero, z figlio dx
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)
                # Caso 3: zio nero, z figlio sx
                    z.parent.color = self.BLACK 
                    z.parent.parent.color = self.RED
                    self.rotate_right(z.parent.parent)
                # Caso 4: simmetrico, z.parent è figlio dx
            else:
                if z == z.parent.left:
                    z = z.parent
                    self.rotate_right(z)
                z.parent.color = self.BLACK
                z.parent.parent.color = self.RED
                self.rotate_left(z.parent.parent)
            # radice sempre nera
        self.root.color = self.BLACK


    def _get_sibling(self, node):                   # identifica nodo fratello per facilitare rotazioni e ricolorazioni
        if node is None or node.parent is None:
            return None
        if node == node.parent.left:                    # se nodo è figlio sx, il fratello è a dx e viceversa
            return node.parent.right
        return node.parent.left
    
    def _rb_switch(self, u, v):                     # u è il nodo da rimuovere, v è il nodo da mettere al suo posto
    # facilita la funzione remove quando bisogna sostituire un nodo con il successore post rimozione
        # Caso 1: u radice di un sottoalbero, v diventa nuova radice
        if u.parent is None:
            self.root = v
        # Caso 2: u è figlio sx, colleghiamo v al lato sx del padre
        elif u == u.parent.left:
            u.parent.left = v
        # Caso 3: u è un figlio dx, colleghiamo v al lato dx del padre
        else:
            u.parent.right = v
        # se v non è un nodo NIL, aggiorniamo puntatore al padre
        if v is not None:
            v.parent = u.parent

# def remove(self, z): 
