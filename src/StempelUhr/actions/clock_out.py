from datetime import datetime
from StempelUhr.services import mysql_verbindung
from StempelUhr.utils import get_user_info


def clock_out(widget, vorname, table):
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
                                (user_id, date, time, 'Aus'))
            conn.commit()
            table.data.append((vorname, nachname, date, time, 'Aus'))
        pass  
    # Schließen Sie die Datenbankverbindung
    cursor.close()
    conn.close()