import streamlit as st
import matplotlib.pyplot as plt

# Titolo dell'app
st.title("Blackjack Card Counter")
st.write("Seleziona il numero di mazzi e le carte per aggiornare il True Count.")

# Selezione del numero di mazzi
mazzi_iniziali = st.number_input("Numero di mazzi", min_value=1, max_value=8, value=1, step=1)

# Definizione del conteggio Hi-Lo
conteggio_hi_lo = {2: +1, 3: +1, 4: +1, 5: +1, 6: +1,
                   7: 0, 8: 0, 9: 0, 10: -1, 11: -1}

# Inizializzazione del conteggio e storico
if "running_count" not in st.session_state:
    st.session_state.running_count = 0
    st.session_state.carte_girate = 0
    st.session_state.history = []

# Funzione per aggiornare il True Count
def aggiorna_conteggio(carta):
    st.session_state.running_count += conteggio_hi_lo.get(carta, 0)
    st.session_state.carte_girate += 1
    mazzi_rimanenti = max(mazzi_iniziali - (st.session_state.carte_girate / 52), 1)
    true_count = st.session_state.running_count / mazzi_rimanenti
    st.session_state.history.append(true_count)

# Creazione dei pulsanti per selezionare la carta
st.write("Clicca su una carta per aggiornare il conteggio:")
col1, col2, col3, col4 = st.columns(4)
buttons = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i, card in enumerate(buttons):
    if i < 3:
        with col1:
            if st.button(str(card)):
                aggiorna_conteggio(card)
    elif i < 6:
        with col2:
            if st.button(str(card)):
                aggiorna_conteggio(card)
    elif i < 9:
        with col3:
            if st.button(str(card)):
                aggiorna_conteggio(card)
    else:
        with col4:
            if st.button(str(card)):
                aggiorna_conteggio(card)

# Mostra il True Count attuale
st.write(f"**Running Count:** {st.session_state.running_count}")
mazzi_rimanenti = max(mazzi_iniziali - (st.session_state.carte_girate / 52), 1)
true_count = st.session_state.running_count / mazzi_rimanenti
st.write(f"**True Count:** {true_count:.2f}")
st.write(f"**Mazzi rimanenti:** {mazzi_rimanenti:.2f}")

# Grafico del True Count
fig, ax = plt.subplots()
ax.plot(st.session_state.history, marker='o', linestyle='-', color='blue')
ax.set_xlabel("Numero di carte inserite")
ax.set_ylabel("True Count")
ax.set_title("Andamento del True Count")
ax.grid()
st.pyplot(fig)
