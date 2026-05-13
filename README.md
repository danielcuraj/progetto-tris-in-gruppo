# Tris Game (Python & MySQL)

---

## Autori (Team)
Il progetto è stato realizzato da:
* **Haka Osman**
* **Curaj Daniel**
* **Ceroni Jacopo**

---

## Descrizione del Progetto
Il software è strutturato in modo **modulare** per garantire una netta separazione tra la logica di gioco, la gestione dei dati e l'interfaccia utente. Consente di giocare a Tris tra due utenti locali, registrando ogni mossa e risultato su un database relazionale.

### Architettura del Codice
Il progetto è suddiviso in tre moduli principali:
1.  **`giocoTris.py`**: Contiene la logica "pura" del gioco (gestione scacchiera, verifica vittoria e pareggio).
2.  **`conn_database.py`**: Gestisce tutte le operazioni CRUD e la comunicazione con il database tramite la libreria `pymysql`.
3.  **`main.py`**: Il punto di ingresso dell'applicazione che gestisce il menu principale e l'esperienza utente.

---

## Funzionalità Principali

* **Gestione Giocatori**: Registrazione automatica dei nuovi giocatori o recupero dei profili esistenti per evitare duplicati.
* **Logica di Gioco Robusta**:
    * Validazione delle mosse (impedisce sovrascritture o input fuori range).
    * Controllo istantaneo delle 8 combinazioni vincenti.
* **Persistenza dei Dati**: Ogni partita viene salvata con data, ID dei giocatori e vincitore.
* **Analisi e Statistiche**:
    *  **Top 5**: Visualizzazione dei migliori 5 giocatori per numero di vittorie.
    * **Statistiche Personali**: Calcolo automatico di partite giocate, vinte, perse e del **Win Rate (%)**.

---

##  Struttura del Database
Il database è composto da due tabelle principali collegate tra loro:

| Tabella | Descrizione |
| :--- | :--- |
| **`giocatore`** | Memorizza l'anagrafica (ID, Nome). |
| **`partita`** | Memorizza i match, collegando i giocatori tramite chiavi esterne (FK). |

---

##  Installazione e Utilizzo

### 1. Prerequisiti
Assicurati di avere installato:
* **Python 3.x**
* **MySQL** o **MariaDB**
* Libreria `pymysql`:
    ```bash
    pip install pymysql
    ```

### 2. Setup del Database
Esegui lo script SQL fornito (`tabelle.sql`) nel tuo client MySQL per creare la struttura necessaria:
```sql
-- Esempio di creazione tabelle
CREATE TABLE giocatore (...);
CREATE TABLE partita (...);

