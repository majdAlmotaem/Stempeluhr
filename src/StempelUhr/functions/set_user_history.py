from StempelUhr.classes.state import state
from .get_user_info import get_user_info
from .message_alert import show_alert
from .get_user_history import get_user_history

def set_user_history(vorname, table):
        # Benutzerinformationen abrufen
    nachname = get_user_info(vorname)

    if nachname:
        # Historie aus der Datenbank abrufen
        history = get_user_history(vorname, nachname)

        # Historie in die Tabelle einfügen
        for entry in history:
            date, time, typ = entry
            table.data.append((vorname, nachname, date, time, typ))
    else:
        show_alert(state.main_window, "Fehler", "Benutzerhistorie konnte nicht abgerufen werden.")
