import random
import time 
import statistics

from RBT import RBT
from AVL import AVL
from BST import BST, TreeNode



#this class can generate trees with n number of keys

class TreeManager():
    def __init__(self, n):
        # creo array [0, 1, 2, ..., n]
        self.keys_array = list(range(n + 1))
        self.m = 0
 
    #this method creates a tree with keys from 0 to n in a random order.
    #TODO this method should return the tree!! 
    #cost O(n * log n)
    def create_rbt(self):
        tree = RBT.__init__()
        n = len(self.keys_array)
        #creates the tree and the two zones of the array [ tree_keys | m | external_keys ]
        for i in range(0, n):
            #generating the random integer in the range(m, n-1)
            j = random.randrange(self.m, n)
            #insert of the key into the tree
            tree.insert(self.keys_array[j])
            #swapping the elements
            self.keys_array[j], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j]
            #increasing the index for the tree_keys zone
            self.m = self.m + 1

    def create_avl(self, n):
        tree = AVL.__init__()
        n = len(self.keys_array)
        #creates the tree and the two zones of the array [ tree_keys | m | external_keys ]
        for i in range(0, n):
            #generating the random integer in the range(m, n-1)
            j = random.randrange(self.m, n)
            #insert of the key into the tree
            tree.insert(self.keys_array[j])
            #swapping the elements
            self.keys_array[j], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j]
            #increasing the index for the tree_keys zone
            self.m = self.m + 1

    def create_bst(self, n):
        tree = BST.__init__()
        n = len(self.keys_array)
        #creates the tree and the two zones of the array [ tree_keys | m | external_keys ]
        for i in range(0, n):
            #generating the random integer in the range(m, n-1)
            j = random.randrange(self.m, n)
            #insert of the key into the tree
            tree.insert(self.keys_array[j])
            #swapping the elements
            self.keys_array[j], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j]
            #increasing the index for the tree_keys zone
            self.m = self.m + 1


    # popola albero (BST/AVL/RBT) con n nodi estratti random, unisce in un'unica funzione la creazione di uno dei tree alberi
    # complessità O(n * log n) 
    def create_tree(self, tree, n):        
        self.m = 0                                  # no chiavi nell'albero
        for i in range(n):
            j = random.randrange(self.m, len(self.keys_array))               # prendo indice a caso e relativa chiave
            chiave_estratta = self.keys_array[j]
            nuovo_nodo = TreeNode(chiave_estratta)                          # creo nodo richiesto e lo inserisco nell'albero + swap col muro
            tree.insert(nuovo_nodo)
            self.keys_array[j], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j]       
            self.m += 1                                                     # traslo muro di una pos. in avanti così da ammettere un elemento all'interno 
            

    # esegue algoritmo C delle opzioni proposte: batch di inserimenti e rimozioni
    # misura tempo mediano di una singola insert su un albero che contiene sempre dimensione n
    def measure_insert(self, tree, batch_size=100):             # scelto 100 come numero per convenienza, numero di volte in cui ripetere il test
        tempi = []
        for _ in range(batch_size):
            # 1- inizializzo misurazione e la effettuo
            # prendo chiave dalla zona fuori, creo nodo relativo e lo inserisco
            j_in = random.randrange(self.m, len(self.keys_array))           
            chiave_da_inserire = self.keys_array[j_in]
            nodo_in = TreeNode(chiave_da_inserire)
            # start e stop del cronometro per misurare inserimento + salvo misurazione
            start = time.perf_counter()
            tree.insert(nodo_in)                    # inserisce in base all'albero in questione
            stop = time.perf_counter()
            tempi.append(stop - start)
            # aggiorno array e swappo il muro facendolo avanzare
            self.keys_array[j_in], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j_in]
            self.m += 1
            # 2- ripristino dimensione albero
            # prendo una chiave dalla zona interna, la ricerco e rimuovo il nodo se esiste
            j_out = random.randrange(0, self.m)
            chiave_da_rimuovere = self.keys_array[j_out]
            nodo_out = tree.find(chiave_da_rimuovere)     # ricerca in base all'albero in questione
            if nodo_out:
                tree.remove(nodo_out)               # rimuove in base all'albero in questione
            # aggiorno array facendo arretrare il muro
            self.m -= 1
            self.keys_array[j_out], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j_out]
        # restituisco mediana dei tempi come da richiesta
        return statistics.median(tempi)

        
    # in create_tree pesco un indice e inserisco la chiave relativa nell'array, swappo col muro e poi traslo --> costo O(1)
    # in measure_insert misuro il tempo medio di una insert: aggiungo nodo, sposto muro, misuro tempo dell'inserimento, cerco nodo, rimuovo nodo !


    # per la logica del muro: se il pc prende n random a un certo punto (soprattutto verso la fine) inizia a pescare numeri che prob. sono già dentro l'albero
    # quindi rischia di andare in loop... per questo mettiamo tutte le chiavi in un array e ci mettiamo un MURO che differenza le chiavi dentro all'albero
    # e quelle fuori. così facendo quando inserisco una chiave sposto il MURO in avanti (verso dx, inizialmente è tutto a sx) e poi quando tolgo una chiave 
    # lo sposto indietro (verso sx). randomizzo la pescata solo su chiavi che sono pefforza fuori dall'albero quindi ez non ho loop o crash o puzzo.
 

