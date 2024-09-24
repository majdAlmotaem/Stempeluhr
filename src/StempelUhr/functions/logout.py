from StempelUhr.classes.state import state

def logout(widget):
    # Vermeide zirkulären Import, indem du den Import innerhalb der Funktion machst
    from .create_starter_window import create_starter_window
    
    # Leert das Hauptfenster und zeigt wieder das Startfenster (Login/Registrierung)
    state.main_window.content = create_starter_window()
    # Aktualisiere den Titel des Hauptfensters
    state.main_window.title = "Login / Registrierung"

    state.main_window.title = "Login / Registrierung"

