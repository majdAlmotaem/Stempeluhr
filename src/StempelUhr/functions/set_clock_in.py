from datetime import datetime
from .mysql_verbindung import *
from .get_user_info import get_user_info

   
def set_clock_in(widget, vorname, table):
    current_datetime = datetime.now()
    date = current_datetime.strftime('%Y-%m-%d')
    time = current_datetime.strftime('%H:%M:%S')
    conn , cursor = mysql_verbindung()
    
    # Benutzerinformationen abrufen
    nachname = get_user_info(vorname)  # Nur den Nachnamen holen

    if nachname:
        # Benutzer-ID holen
        cursor.execute('SELECT id FROM user WHERE vorname = %s AND nachname = %s', (vorname, nachname))
        user_id = cursor.fetchone()
        if user_id:
            user_id = user_id[0]
            # Daten in der Datenbank speichern
            cursor.execute('INSERT INTO stempel (benutzer_id, datum, uhrzeit, typ) VALUES (%s, %s, %s, %s)',
                                (user_id, date, time, 'Ein'))
            conn.commit()
            table.data.append((vorname, nachname, date, time, 'Ein'))
        pass
    # Schließen Sie die Datenbankverbindung
    cursor.close()
    conn.close()