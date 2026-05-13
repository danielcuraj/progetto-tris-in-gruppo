# progetto-tris-in-gruppo
TRIS
Autori: Haka Osman, Curaj Daniel, Ceroni Jacopo

DESCRIZIONE
Il progetto consiste in un’applicazione desktop del gioco del Tris realizzata in Python con interfaccia da terminale (CLI). Il software è strutturato in modo modulare, separando nettamente la logica di gioco (giocoTris.py), la gestione del database (conn_database.py) e il menu principale (main.py).
Funzionamento del Gioco
All'avvio di una nuova partita, il sistema richiede l'inserimento dei nomi dei due partecipanti (Giocatore X e Giocatore O). Il programma gestisce le mosse tramite coordinate numeriche da 0 a 8, corrispondenti alle celle della scacchiera.
Validazione: Il software impedisce l'inserimento di mosse in celle già occupate o fuori dal range consentito.
Controllo Vittoria: Al termine di ogni turno, vengono analizzate le 8 combinazioni vincenti (righe, colonne e diagonali).
Esito: La partita termina con la vittoria di uno dei due giocatori o con un pareggio nel caso in cui la scacchiera venga completata senza un vincitore.
Integrazione Database MySQL
Il cuore del progetto è la persistenza dei dati. Tramite la libreria pymysql, il programma si connette a un database MariaDB/MySQL per memorizzare lo storico delle attività:
Tabella giocatore: Registra l'anagrafica (ID, Cognome, Nome). Se un giocatore ha già giocato in passato, il sistema lo riconosce senza creare duplicati.
Tabella partita: Memorizza ogni match giocato, associando gli ID dei giocatori al risultato finale e alla data corrente.
Relazioni: Il sistema utilizza chiavi esterne per garantire l'integrità dei dati tra le tabelle.
Analisi e Statistiche
Oltre al gioco, il software permette di consultare i dati archiviati:
Classifica Top 5: Una query SQL estrae i 5 giocatori con il maggior numero di vittorie totali.
Statistiche Personali: Cercando un giocatore per nome, è possibile visualizzare il numero totale di partite giocate, vinte e perse, calcolando automaticamente il Win Rate percentuale (rapporto vittorie/partite totali).

