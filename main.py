from giocoTris import gioca_partita
from conn_database import (
    get_or_create_giocatore,
    get_giocatore_by_id,
    salva_partita,
    get_top_5_giocatori,
    get_statistiche_giocatore
)

def menu_principale():
    while True:
        print("\n" + "="*40)
        print("TRIS - MENU PRINCIPALE")
        print("="*40)
        print("1. Gioca una partita")
        print("2. Visualizza top 5 giocatori")
        print("3. Visualizza statistiche personali")
        print("4. Esci")
        print("="*40)
        
        scelta = input("Seleziona un'opzione (1-4): ").strip()
        
        if scelta == "1":
            gestisci_partita()
        elif scelta == "2":
            mostra_top_5()
        elif scelta == "3":
            mostra_statistiche_personali()
        elif scelta == "4":
            print("\nArrivederci! 👋")
            break
        else:
            print("Opzione non valida. Riprova.")

def gestisci_partita():
    print("\n" + "-"*40)
    print("NUOVA PARTITA")
    print("-"*40)
    
    nome_x = input("Nome del giocatore X: ").strip()
    if not nome_x:
        print("Nome non valido.")
        return
    
    nome_o = input("Nome del giocatore O: ").strip()
    if not nome_o:
        print("Nome non valido.")
        return
    
    print("\nCreazione/recupero giocatori dal database...")
    id_x = get_or_create_giocatore(nome_x)
    id_o = get_or_create_giocatore(nome_o)
    
    vincitore, _ = gioca_partita()
    
    print("\nSalvataggio del risultato nel database...")
    salva_partita(id_x, id_o, vincitore)
    print("Partita salvata nel database!")

def mostra_top_5():
    print("\n" + "-"*40)
    print("TOP 5 GIOCATORI")
    print("-"*40)
    
    risultati = get_top_5_giocatori()
    
    if not risultati:
        print("Nessuna partita registrata nel database.")
        return
    
    print(f"\n{'Posizione':<12} {'Giocatore':<30} {'Vittorie':<10}")
    print("-" * 50)
    
    for i, (nome, vittorie) in enumerate(risultati, 1):
        print(f"{i:<12} {nome:<30} {vittorie:<10}")
    print()

def mostra_statistiche_personali():
    print("\n" + "-"*40)
    print("STATISTICHE PERSONALI")
    print("-"*40)
    
    nome_giocatore = input("Inserisci il nome del giocatore: ").strip()
    if not nome_giocatore:
        print("Nome non valido.")
        return
    
    id_giocatore = get_or_create_giocatore(nome_giocatore)
    
    giocatore = get_giocatore_by_id(id_giocatore)
    if not giocatore:
        print("Giocatore non trovato.")
        return
    
    id_g, nome = giocatore
    stats = get_statistiche_giocatore(id_giocatore)
    
    print(f"\n{'Giocatore:':<25} {nome}")
    print(f"{'Partite giocate:':<25} {stats['partite_giocate']}")
    print(f"{'Partite vinte:':<25} {stats['partite_vinte']}")
    print(f"{'Partite perse:':<25} {stats['partite_perse']}")
    print(f"{'Pareggi:':<25} {stats['partite_giocate'] - stats['partite_vinte'] - stats['partite_perse']}")
    print(f"{'Win Rate:':<25} {stats['win_rate']}%")
    print()

if __name__ == "__main__":
    try:
        menu_principale()
    except KeyboardInterrupt:
        print("\n\nProgramma interrotto.")
    except Exception as e:
        print(f"\nErrore: {e}")
