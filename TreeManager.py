import random

from RBT import rbt
from AVL import avl
from BST import bst
#this class can generate trees with n number of keys
class TreeManager():
    def __init__(self, n):
        self.keys_array = []
        #creates the array [0, ... , 2n - 1]
        for i in range(0, n+1):
            self.keys_array.insert(i)
        #index for the tree keys
        self.m = 0
        
        

    #this method creates a tree with keys from 0 to n in a random order.
    #TODO this method should return the tree!! 
    #cost O(n * log n)
    def create_rbt(self):
        tree = rbt.__init__()
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
        tree = avl.__init__()
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
        tree = bst.__init__()
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

    #

        

            #inizializzo manager creo un rbt, avl e bst, testo, costruisco un array per ciascun albero con i tempi, analizzo i tempi mettendoli su un grafo excel
        
        
        
