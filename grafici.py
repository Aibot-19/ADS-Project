import csv
import matplotlib.pyplot as plt 

def main():
    # Liste per memorizzare i dati letti dal CSV
    n_values = []
    bst_times = []
    avl_times = []
    rbt_times = []

    # 1. Lettura dei dati dal file CSV
    print("Lettura dei dati da 'misurazioni_alberi.csv'...")
    try:
        with open('misurazioni_alberi.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader) # Salta la prima riga (l'intestazione con i nomi delle colonne)
            
            for row in reader:
                # Convertiamo le stringhe lette dal CSV in numeri (float e int)
                n_values.append(int(row[0]))
                bst_times.append(float(row[1]))
                avl_times.append(float(row[2]))
                rbt_times.append(float(row[3]))
    except FileNotFoundError:
        print("Errore: Il file 'misurazioni_alberi.csv' non è stato trovato.")
        return

    # 2. Creazione del grafico
    print("Generazione del grafico in corso...")
    
    # Imposta la dimensione della figura (in pollici, proporzione adatta per A4)
    plt.figure(figsize=(10, 6))

    # Traccia le tre linee (aggiungiamo dei piccoli marker per vedere i punti effettivi)
    plt.plot(n_values, bst_times, label='BST (Albero Binario Semplice)', color='blue', marker='o', markersize=3, linewidth=1.5)
    plt.plot(n_values, avl_times, label='AVL', color='red', marker='s', markersize=3, linewidth=1.5)
    plt.plot(n_values, rbt_times, label='RBT (Red-Black Tree)', color='green', marker='^', markersize=3, linewidth=1.5)

    # 3. Personalizzazione degli assi
    # Questa è la parte fondamentale: usiamo una scala logaritmica per l'asse X
    # perché abbiamo generato n usando una progressione geometrica.
    plt.xscale('log')
    
    # Titoli e etichette
    plt.title('Tempo mediano di Inserimento in funzione della dimensione $n$', fontsize=14, pad=15)
    plt.xlabel('Dimensione dell\'albero $n$ (scala logaritmica)', fontsize=12)
    plt.ylabel('Tempo mediano di inserimento (secondi)', fontsize=12)

    # Aggiunge una griglia per facilitare la lettura dei valori
    plt.grid(True, which="both", ls="--", alpha=0.5)

    # Aggiunge la legenda (in alto a sinistra di solito è un buon posto se le linee salgono)
    plt.legend(loc='upper left', fontsize=11)

    # 4. Salvataggio e visualizzazione
    # Salva il grafico come PNG per poterlo inserire nel documento LaTeX
    plt.savefig('grafico_tempi.png', dpi=300, bbox_inches='tight')
    print("Grafico salvato come 'grafico_tempi.png'!")


if __name__ == "__main__":
    main()