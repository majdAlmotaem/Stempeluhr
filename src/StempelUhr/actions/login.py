import toga
from StempelUhr.GUI_components.main_window import create_main_ui
from StempelUhr.services import mysql_verbindung
from StempelUhr.utils.message_alert import show_alert


def login(vorname, main_window: toga.MainWindow):
    _, cursor = mysql_verbindung()
    # Überprüfen, ob der Benutzer existiert
    cursor.execute('SELECT vorname FROM user WHERE vorname = %s', (vorname,))
    user = cursor.fetchone()
    
    if user and user[0] == vorname:
        main_window.content = create_main_ui(main_window, vorname)

    else:
        show_alert(main_window, "Fehler", "Sie sind nicht registriert!")