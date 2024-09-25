from .mysql_verbindung import *

def get_user_history(vorname, nachname):
    conn, cursor = mysql_verbindung()

    # SQL-Abfrage zur Historie
    query = '''
    SELECT datum, uhrzeit, typ
    FROM stempel
    JOIN user ON stempel.benutzer_id = user.id
    WHERE user.vorname = %s AND user.nachname = %s
    ORDER BY datum ASC, uhrzeit ASC
    '''

    cursor.execute(query, (vorname, nachname))
    history = cursor.fetchall()  # Alle Einträge abrufen
    
    cursor.close()
    conn.close()

    return history