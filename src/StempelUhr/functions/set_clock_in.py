from datetime import datetime
from .mysql_verbindung import *
from .get_user_info import get_user_info
from .message_alert import show_alert

def set_clock_in(widget, vorname, table):
    current_datetime = datetime.now()
    date = current_datetime.strftime('%Y-%m-%d')
    time = current_datetime.strftime('%H:%M:%S')
    conn, cursor = mysql_verbindung()
    
    # Benutzerinformationen abrufen
    nachname = get_user_info(vorname)  # Nur den Nachnamen holen

    if nachname:
        # Benutzer-ID holen
        cursor.execute('SELECT id FROM user WHERE vorname = %s AND nachname = %s', (vorname, nachname))
        # Benutzer-ID holen
        user_id = cursor.fetchone()
       # Ceckt ob User bereits eingestempelt hat
        if user_id:
            user_id = user_id[0]
            
            # Letzten Eintrag des Benutzers abrufen
            cursor.execute('SELECT typ FROM stempel WHERE benutzer_id = %s ORDER BY id DESC LIMIT 1', (user_id,))
            # Letzten Eintrag des Benutzers abrufen
            last_entry = cursor.fetchone()
            # Ceckt ob User bereits eingestempelt hat
            if last_entry and last_entry[0] == 'Ein':
                show_alert(widget.window, "Fehler", "Sie sind bereits eingestempelt!")
            else:
                # Daten in der Datenbank speichern
                cursor.execute('INSERT INTO stempel (benutzer_id, datum, uhrzeit, typ) VALUES (%s, %s, %s, %s)',
                                (user_id, date, time, 'Ein'))
                conn.commit()
                table.data.append((vorname, nachname, date, time, 'Ein'))
    
    # Schließen der Datenbankverbindung
    cursor.close()
    conn.close()
