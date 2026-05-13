import pymysql
from datetime import datetime

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "4CTL_curaj.d.231108",
    "password": "Forzaviola2026!",
    "database": "4CTL_curaj.d.231108",
    "port": 3307,
    "cursorclass": pymysql.cursors.Cursor,
    "connect_timeout": 5,
}

def get_connection():
    return pymysql.connect(**DB_CONFIG)

def get_or_create_giocatore(nome):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT id_giocatore FROM giocatore WHERE nome = %s"
            cursor.execute(sql, (nome))
            result = cursor.fetchone()
            
            if result:
                return result[0]
            else:
                sql = "INSERT INTO giocatore (nome) VALUES (%s)"
                cursor.execute(sql, (nome))
                conn.commit()
                return cursor.lastrowid
    finally:
        conn.close()

def get_giocatore_by_id(id_giocatore):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT id_giocatore, nome FROM giocatore WHERE id_giocatore = %s"
            cursor.execute(sql, (id_giocatore,))
            return cursor.fetchone()
    finally:
        conn.close()

def salva_partita(id_giocatore_x, id_giocatore_o, vincitore):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """INSERT INTO partita (id_giocatoreX, id_giocatoreO, data_partita, vincitore) 
                     VALUES (%s, %s, %s, %s)"""
            data_partita = datetime.now().date()
            cursor.execute(sql, (id_giocatore_x, id_giocatore_o, data_partita, vincitore))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

def get_top_5_giocatori():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT g.nome, COUNT(p.id_partita) as vittorie
                FROM giocatore g
                LEFT JOIN partita p ON (
                    (p.vincitore = 'X' AND p.id_giocatoreX = g.id_giocatore) OR
                    (p.vincitore = 'O' AND p.id_giocatoreO = g.id_giocatore)
                )
                GROUP BY g.id_giocatore
                ORDER BY vittorie DESC
                LIMIT 5
            """
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def get_statistiche_giocatore(id_giocatore):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """SELECT COUNT(*) FROM partita 
                     WHERE id_giocatoreX = %s OR id_giocatoreO = %s"""
            cursor.execute(sql, (id_giocatore, id_giocatore))
            partite_giocate = cursor.fetchone()[0]
            
            sql = """SELECT COUNT(*) FROM partita WHERE
                     (id_giocatoreX = %s AND vincitore = 'X') OR
                     (id_giocatoreO = %s AND vincitore = 'O')"""
            cursor.execute(sql, (id_giocatore, id_giocatore))
            partite_vinte = cursor.fetchone()[0]
            
            sql = """SELECT COUNT(*) FROM partita WHERE
                     ((id_giocatoreX = %s AND vincitore = 'O') OR
                      (id_giocatoreO = %s AND vincitore = 'X'))"""
            cursor.execute(sql, (id_giocatore, id_giocatore))
            partite_perse = cursor.fetchone()[0]
            
            win_rate = (partite_vinte / partite_giocate * 100) if partite_giocate > 0 else 0
            
            return {
                "partite_giocate": partite_giocate,
                "partite_vinte": partite_vinte,
                "partite_perse": partite_perse,
                "win_rate": round(win_rate, 2)
            }
    finally:
        conn.close()
