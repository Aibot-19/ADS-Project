import random
import time 
import statistics

from BST import TreeNode



# this class can generate trees with n number of keys

class TreeManager():
    def __init__(self, n):
        # creates array [0, 1, 2, ..., n]
        self.keys_array = list(range(n + 1))
        self.m = 0
 
    # populates tree (BST/AVL/RBT) with n nodes random extracted, combines in a single function the creation of one of the trees
    # time complexity O(n * log n) 
    def create_tree(self, tree):        
        self.m = 0 
        n = len(self.keys_array) - 1                        # no keys in the tree
        for i in range(n):
            j = random.randrange(self.m, len(self.keys_array))               # takes random index and relative key
            chiave_estratta = self.keys_array[j]
            nuovo_nodo = TreeNode(chiave_estratta)                          # creates requested node and inserts it in the tree + swaps it with wall
            tree.insert(nuovo_nodo)
            self.keys_array[j], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j]       
            self.m += 1                                                     # moves the wall of 1 position forward, admits an element inside

    # executes C algorithm: batch of insert and remove 
    # measures median time of a single insert on a tree that always has size n
    def measure_insert(self, tree, batch_size=100):             # choosed 100 to be batch_size for convenience, number of iteration of the test
        tempi = []
        for _ in range(batch_size):
            # 1- inizializes measurement and executes it
            # takes key from out zone, creates relative node and inserts it
            j_in = random.randrange(self.m, len(self.keys_array))           
            chiave_da_inserire = self.keys_array[j_in]
            nodo_in = TreeNode(chiave_da_inserire)
            # starts and stops chronometer to measure insert, saves measurement 
            start = time.perf_counter()
            tree.insert(nodo_in)                    # insert function of relative type of tree 
            stop = time.perf_counter()
            tempi.append(stop - start)
            # updates array and swaps wall to make it move forward 
            self.keys_array[j_in], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j_in]
            self.m += 1
            # 2- restores tree size 
            # takes key from internal zone, searchs it and removes relative node (if it exists)
            j_out = random.randrange(0, self.m)
            chiave_da_rimuovere = self.keys_array[j_out]
            nodo_out = tree.find(chiave_da_rimuovere)     # search function of relative type of tree 
            if nodo_out:
                tree.remove(nodo_out)               # remove function of relative type of tree
            # updates array and moves wall backwards
            self.m -= 1
            self.keys_array[j_out], self.keys_array[self.m] = self.keys_array[self.m], self.keys_array[j_out]
        # returns median of time 
        return statistics.median(tempi)

        
    