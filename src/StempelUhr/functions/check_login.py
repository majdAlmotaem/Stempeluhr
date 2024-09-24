import toga
from .create_main_window import create_main_window
from .mysql_verbindung import mysql_verbindung
from .message_alert import show_alert
from StempelUhr.classes.state import state


def check_login(vorname):
    _, cursor = mysql_verbindung()
    # Überprüfen, ob der Benutzer existiert
    cursor.execute('SELECT vorname FROM user WHERE vorname = %s', (vorname,))
    user = cursor.fetchone()
    
    if user and user[0] == vorname:
        # Greife auf state.main_window zu, anstatt main_window als Parameter zu übergeben
        state.main_window.content = create_main_window(vorname)
        state.main_window.title = 'Zeiterfassung'
        state.main_window.size = (400, 600)  # Fenstergröße anpassen
    else:
        show_alert(state.main_window, "Fehler", "Sie sind nicht registriert!")