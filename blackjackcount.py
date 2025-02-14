import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# Definizione del conteggio Hi-Lo
conteggio_hi_lo = {2: +1, 3: +1, 4: +1, 5: +1, 6: +1,
                   7: 0, 8: 0, 9: 0,
                   10: -1, 11: -1}

# Variabili di gioco
running_count = 0
history = []
mazzi_iniziali = 1  # Numero iniziale di mazzi
carte_girate = 0
output_area = widgets.Output()

def aggiorna_conteggio(carta):
    global running_count, history, carte_girate, mazzi_iniziali
    if carta in conteggio_hi_lo:
        running_count += conteggio_hi_lo[carta]
        carte_girate += 1
        mazzi_rimanenti = max(mazzi_iniziali - (carte_girate / 52), 1)
        true_count = running_count / mazzi_rimanenti
        history.append(true_count)

        # Aggiorna l'output
        with output_area:
            clear_output(wait=True)
            print(f"Carta selezionata: {carta}")
            print(f"Running Count attuale: {running_count}")
            print(f"True Count attuale: {true_count:.2f}")
            print(f"Mazzi rimanenti: {mazzi_rimanenti:.2f}")

            # Aggiorna il grafico
            plt.figure(figsize=(8, 4))
            plt.plot(history, marker='o', linestyle='-', color='blue')
            plt.xlabel("Numero di carte inserite")
            plt.ylabel("True Count")
            plt.title("Andamento del True Count")
            plt.grid()
            plt.show()
    else:
        with output_area:
            clear_output(wait=True)
            print("Carta non valida.")

# Selezione del numero di mazzi
mazzi_selector = widgets.BoundedIntText(value=1, min=1, max=8, step=1, description='Mazzi:')
def set_mazzi(_):
    global mazzi_iniziali
    mazzi_iniziali = mazzi_selector.value
    with output_area:
        clear_output(wait=True)
        print(f"Numero di mazzi impostato: {mazzi_iniziali}")

mazzi_button = widgets.Button(description="Conferma Mazzi")
mazzi_button.on_click(set_mazzi)

# Creazione dei pulsanti per selezionare la carta
buttons = []
for card in range(2, 12):
    btn = widgets.Button(description=str(card))
    btn.on_click(lambda _, c=card: aggiorna_conteggio(c))
    buttons.append(btn)

# Layout per i pulsanti
grid = widgets.HBox(buttons)

display(mazzi_selector, mazzi_button, grid, output_area)
