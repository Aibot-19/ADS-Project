import csv
import math 

from BST import BST
from AVL import AVL 
from RBT import RBT 

from TreeManager import TreeManager 

def main():
    #valore minimo di n
    n_min = 1000
    #valore massimo di n
    n_max = 10000000
    #calcolo la costante c
    c = pow((n_max/n_min), (1/99))
    #creo gli array per salvare i dati delle misurazioni dei tempi per ciascun array
    bst_times = []
    avl_times = []
    rbt_times = []
    n_values = []

    for i in range(0, 100):
        #creo il valore i-esimo della progressione geometrica
        n_i = math.floor(n_min * pow(c, i))
        n_values.insert(i, n_i)
        #creo il tree-manager composto da n_i chiavi
        tm = TreeManager(n_i)
        #creo gli alberi
        bst = BST()
        avl = AVL()
        rbt = RBT()
        #popolo gli alberi per un totale di n_i chiavi
        tm.create_tree(bst, n_i)
        tm.create_tree(avl, n_i)
        tm.create_tree(rbt, n_i)
        #misuro i tempi e inserisco questi tempi all'interno dell'i-esima cella dell'array
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