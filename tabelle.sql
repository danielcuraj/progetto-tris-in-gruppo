CREATE TABLE giocatore(
id_giocatore INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome VARCHAR(50) NOT NULL
);

CREATE TABLE partita(
id_partita INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
id_giocatoreX INT NOT NULL,
id_giocatoreO INT NOT NULL,
vincitore VARCHAR(50) NOT NULL,
FOREIGN KEY (id_giocatoreX) REFERENCES giocatore(id_giocatore),
FOREIGN KEY (id_giocatoreO) REFERENCES giocatore(id_giocatore)
);

