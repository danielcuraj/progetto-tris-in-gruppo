"""
Modulo logica del gioco Tris - Separato dalla logica di database
Contiene solo funzioni pure per la logica di gioco
"""


def crea_scacchiera():
    """Restituisce una nuova scacchiera vuota."""
    return ["_"] * 9


def stampa_scacchiera(scacchiera):
    """Stampa la scacchiera in formato leggibile."""
    print(f"\n {scacchiera[0]} | {scacchiera[1]} | {scacchiera[2]}")
    print(f"-----------")
    print(f" {scacchiera[3]} | {scacchiera[4]} | {scacchiera[5]}")
    print(f"-----------")
    print(f" {scacchiera[6]} | {scacchiera[7]} | {scacchiera[8]}\n")


def fai_mossa(scacchiera, posizione, giocatore):
    """
    Effettua una mossa sulla scacchiera.
    
    Args:
        scacchiera (list): Lista di 9 elementi rappresentante la scacchiera
        posizione (int): Posizione da 0 a 8
        giocatore (str): "X" o "O"
    
    Returns:
        bool: True se la mossa è valida, False altrimenti
    """
    if scacchiera[posizione] == "_":
        scacchiera[posizione] = giocatore
        return True
    else:
        return False


def ha_vinto(scacchiera, giocatore):
    """
    Controlla se un giocatore ha vinto.
    
    Args:
        scacchiera (list): Lista di 9 elementi rappresentante la scacchiera
        giocatore (str): "X" o "O"
    
    Returns:
        bool: True se il giocatore ha vinto, False altrimenti
    """
    combinazioni_vincenti = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Righe
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonne
        [0, 4, 8], [2, 4, 6]              # Diagonali
    ]
    
    for combo in combinazioni_vincenti:
        if (scacchiera[combo[0]] == scacchiera[combo[1]] == scacchiera[combo[2]] == giocatore):
            return True
    return False


def scacchiera_piena(scacchiera):
    """
    Controlla se la scacchiera è piena.
    
    Args:
        scacchiera (list): Lista di 9 elementi
    
    Returns:
        bool: True se piena, False altrimenti
    """
    return "_" not in scacchiera


def gioca_partita():
    """
    Esegue una partita completa di Tris.
    La logica è pura e separata dal database.
    
    Returns:
        tuple: (vincitore, scacchiera_finale) dove vincitore è "X", "O" o "P" (pareggio)
    """
    scacchiera = crea_scacchiera()
    giocatore_corrente = "X"
    mosse_fatte = 0

    print("\nBenvenuto a Tris! Inserisci un numero da 0 a 8 per muovere.")
    print("Layout della scacchiera:")
    print(" 0 | 1 | 2")
    print("-----------")
    print(" 3 | 4 | 5")
    print("-----------")
    print(" 6 | 7 | 8\n")

    while True:
        stampa_scacchiera(scacchiera)
        
        try:
            mossa = int(input(f"Turno di {giocatore_corrente}. Inserisci posizione (0-8): "))
            
            if mossa < 0 or mossa > 8:
                print("Errore: il numero deve essere tra 0 e 8!")
                continue
            
            if fai_mossa(scacchiera, mossa, giocatore_corrente):
                mosse_fatte += 1
                
                # Controllo vittoria
                if ha_vinto(scacchiera, giocatore_corrente):
                    stampa_scacchiera(scacchiera)
                    print(f"Complimenti! Il giocatore {giocatore_corrente} ha vinto!")
                    return giocatore_corrente, scacchiera
                
                # Controllo pareggio
                if scacchiera_piena(scacchiera):
                    stampa_scacchiera(scacchiera)
                    print("Pareggio!")
                    return "P", scacchiera
                
                # Cambio turno
                giocatore_corrente = "O" if giocatore_corrente == "X" else "X"
            else:
                print("Cella già occupata! Riprova.")
        
        except ValueError:
            print("Input non valido! Inserisci un numero intero.")
