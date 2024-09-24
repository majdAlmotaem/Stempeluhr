import toga
from .mysql_verbindung import mysql_verbindung
from .message_alert import show_alert

def register(vorname, nachname,widget):
    
    if not vorname or not nachname:
        show_alert(widget.window, "Fehler", "Bitte füllen Sie beide Felder aus!")
        return
    
    conn, cursor = mysql_verbindung()

    # Überprüfen, ob der Vorname und Nachname bereits existieren
    cursor.execute('SELECT * FROM user WHERE vorname = %s AND nachname = %s', (vorname, nachname))
    # Überprüfen, ob der Vorname und Nachname bereits existieren
    user = cursor.fetchone()
    
    # Wenn der Benutzer bereits existiert, zeige eine Fehlermeldung
    if user:
        # Wenn der Benutzer bereits existiert, zeige eine Fehlermeldung
        show_alert(widget.window, "Registrierung fehlgeschlagen", "Benutzer existiert bereits!")
    else:
        # Wenn der Benutzer nicht existiert, füge ihn in die Datenbank ein
        cursor.execute('INSERT INTO user (vorname, nachname) VALUES (%s, %s)', (vorname, nachname))
        conn.commit()
        show_alert(widget.window, "Registrierung erfolgreich", "Benutzer wurde erfolgreich registriert!")

    cursor.close()
    conn.close()