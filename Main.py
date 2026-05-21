import csv
import math 

from BST import BST
from AVL import AVL 
from RBT import RBT 

from TreeManager import TreeManager 

def main():
    # minimum value of n 
    n_min = 1000
    # maximum value of n 
    n_max = 10000000
    # calculates c costant 
    c = pow((n_max/n_min), (1/99))
    # creates arrays to save measurement datas (for each array/tree)
    bst_times = []
    avl_times = []
    rbt_times = []
    n_values = []

    for i in range(0, 100):
        # creates the i-th value of the geometric progression
        n_i = math.floor(n_min * pow(c, i))
        n_values.insert(i, n_i)
        # creates tree_manager composed of n_i keys
        tm = TreeManager(n_i)
        # creates trees
        bst = BST()
        avl = AVL()
        rbt = RBT()
        # populates trees with a total of n_i keys
        tm.create_tree(bst, n_i)
        tm.create_tree(avl, n_i)
        tm.create_tree(rbt, n_i)
        # measures times and inserts them inside of array's i-th cell 
        bst_times.insert(i, tm.measure_insert(bst))
        print(bst_times[i])
        avl_times.insert(i, tm.measure_insert(avl))
        print(avl_times[i])
        rbt_times.insert(i, tm.measure_insert(rbt))
        print(rbt_times[i])

    with open('misurazioni_alberi.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['Dimensione_N', 'Tempo_BST', 'Tempo_AVL', 'Tempo_RBT'])

        for i in range(0, 100):
            row = [n_values[i], bst_times[i], avl_times[i], rbt_times[i]]
            writer.writerow(row)

    print("dati salvati con successo in 'misurazioni_alberi.csv'")

    

if __name__ == "__main__":
    main()