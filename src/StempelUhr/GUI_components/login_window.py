import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime

class login:
    

    def create_login_ui(self):
            # Komponenten für das Login/Registrierungsfenster
            self.vorname_input = toga.TextInput(placeholder="Vorname", style=Pack(padding=5))
            self.nachname_input = toga.TextInput(placeholder="Nachname", style=Pack(padding=5))
            self.login_button = toga.Button('Login', on_press=self.login, style=Pack(padding=10))
            self.register_button = toga.Button('Registrieren', on_press=self.register, style=Pack(padding=10))

            # Layout für das Login/Registrierungsfenster
            login_box = toga.Box(
                children=[self.vorname_input, self.nachname_input, self.login_button, self.register_button],
                style=Pack(direction=COLUMN, alignment=CENTER, padding=20)
            )
            self.main_window.content = login_box

