# state.py

class AppState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
            cls.main_window = None  # Speicher für das Hauptfenster
        return cls._instance

# Globale Instanz
state = AppState()
