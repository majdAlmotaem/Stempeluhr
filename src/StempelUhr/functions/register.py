import toga
from .mysql_verbindung import mysql_verbindung

def register(vorname, nachname,widget):
    conn, cursor = mysql_verbindung()
    cursor.execute('INSERT INTO user (vorname, nachname) VALUES (%s, %s)', (vorname, nachname))
    conn.commit()
    cursor.close()
    conn.close()