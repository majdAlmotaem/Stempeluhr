import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime
from StempelUhr.classes.state import state
from .check_login import check_login
from .register import register


def create_starter_window():
    # Komponenten für das Login/Registrierungsfenster
    vorname_input = toga.TextInput(placeholder="Vorname", style=Pack(padding=5))
    nachname_input = toga.TextInput(placeholder="Nachname", style=Pack(padding=5))
    login_button = toga.Button('Login', style=Pack(padding=10))
    login_button.on_press = lambda widget: check_login(vorname_input.value)   
    register_button = toga.Button('Registrieren', style=Pack(padding=10))
    register_button.on_press = lambda widget: register(vorname_input.value, nachname_input.value, widget)
    # Layout für das Login/Registrierungsfenster
    login_box = toga.Box(
        children=[vorname_input, nachname_input, login_button, register_button],
        style=Pack(direction=COLUMN, alignment=CENTER, padding=20)
    )
    return login_box
