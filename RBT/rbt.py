from BST import BST, TreeNode

def color(node):
    return getattr(node, "color", "black") if node != None else "black" 

class RBTree(BST):
    def __init__(self, root=None):
        super().__init__(root)

    def _get_color(self, node):                 # restituisce colore nodo, se è None (NIL) è nero
        if node is None:
            return "black"
        return getattr(node, 'color', "black")
    
    def _set_color(self, node, color_string):          # assegna colore a nodo, se esiste
        if node is not None:
            node.color = color_string


    def insert(self, node):
        self._set_color(node, "red")                # nuovi nodi sono rossi
        super().insert(node)
        self._fix_insert(node)

    def _fix_insert(self, z):                   # risolve gli errori post inserimento
        while z.parent and self._get_color(z.parent) == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right           # è lo zio
                # Caso 1: zio rosso
                if self._get_color(y) == "red":
                    self._set_color(z.parent, "black")
                    self._set_color(y, "black")
                    self._set_color(z.parent.parent, "red")
                    z = z.parent.parent
                # Caso 2: zio nero, z figlio dx
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)
                # Caso 3: zio nero, z figlio sx
                    self._set_color(z.parent, "black")
                    self._set_color(z.parent.parent, "red")
                    self.rotate_right(z.parent.parent)
                # Caso 4: simmetrico, z.parent è figlio dx
            else:
                y = z.parent.parent.left      # casi simmetrici
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


    def remove(self, node):                     # rimuove nodo da albero scambiando puntatori, se era nero l'altezza va sistemata
        y = node
        y_original_color = self._get_color(y)
        # Caso 1: nodo da rimuovere senza figlio sx
        if node.left is None:
            x = node.right                              # nodo che prende il posto di y, se è None uso il padre
            p = node.parent
            self._rb_switch(node, node.right)           # li scambio
        # Caso 2: nodo da rimuovere senza figlio dx
        elif node.right is None:
            x = node.left
            p = node.parent
            self._rb_switch(node, node.left)
        # Caso 3: nodo con due figli, uso il successore
        else:
            y = self.nxt(node)              # trovo successore e memorizzo il suo colore
            y_original_color = self._get_color(y)
            x = y.right                                              # suc è sempre senza figlio sx, suo figlio dx prende il suo posto
            if y.parent == node:                # se il suc è il figlio dx del nodo da rimuovere
                p = y                               # y sarà nuovo padre 
                if x: x.parent = y                  # sistemiamo puntatori
            else:                              # se il successore è più in profondità 
                p = y.parent                        
                self._rb_switch(y, y.right)         # swap di y e suo figlio
                y.right = node.right                # y è nuova radice sottoalbero dx
                y.right.parent = y                  # aggiorno puntatore
                                               # nessuno dei casi precedenti 
            self._rb_switch(node, y)                # sostituisco node con il successore di y
            y.left = node.left                      # y radice sottoalbero sx
            y.left.parent = y
            self._set_color(y, self._get_color(node))   
        
        # ribilancio albero se ho rimosso nodo nero
        if y_original_color == "black":
            self._fix_remove(x, p)

    def _fix_remove(self, x, p):                # ripristina proprietà albero se è stato rimosso nodo nero, x nodo nuovo e p è suo padre
        while x != self.root and self._get_color(x) == "black":
            # x è figlio sinistro di p
            if x == p.left:              
                w = p.right              # fratello di w
                # Caso 1: fratello rosso
                if self._get_color(w) == "red":             # coloro fratello nero e padre rosso, ruoto a sx => sposto x in un altro caso
                    self._set_color(w, "black")
                    self._set_color(p, "red")
                    self.rotate_left(p)
                    w = p.right
                # Caso 2: fratello nero con figli neri
                if self._get_color(w.left) == "black" and self._get_color(w.right) == "black":          # coloro fratello rosso e risalgo verso la radice
                    self._set_color(w, "red")
                    x = p
                    p = x.parent if x else None
                # Caso 3: fratello nero, figlio dx nero e sx rosso
                else:                               # coloro fratello di rosso e figli entrambi neri, ruoto a destra spostandomi nel caso 4
                    if self._get_color(w.right) == "black":
                        self._set_color(w.left, "black")
                        self._set_color(w, "red")
                        self.rotate_right(w)
                        w = p.right
                # Caso 4: fratello nero, diglio dx rosso e sx nero
                    self._set_color(w, self._get_color(p))
                    self._set_color(p, "black")
                    self._set_color(w.right, "black")
                    self.rotate_left(p)
                    x = self.root
            # x è figlio destro di p, simmetria
            else:
                w = p.left          # fratello
                # stessi casi solo simmetrici  
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
        # nodo x (o radice) diventa nero per bilanciare altezza nera
        self._set_color(x, "black")


