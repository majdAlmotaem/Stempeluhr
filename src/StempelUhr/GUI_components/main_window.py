import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime
from StempelUhr.actions.clock_in import clock_in
from StempelUhr.actions.clock_out import clock_out

def create_main_ui(vorname):
    title = 'Zeiterfassung'
    size = (400, 600)  # Fenstergröße anpassen
    
    # Begrüßung erstellen und zentrieren
    greeting_label = toga.Label(
        f"Willkommen, {vorname}!",
        style=Pack(padding=10, text_align="center")
    )
    current_time = datetime.now().strftime("%H:%M")
    # Weitere Komponenten erstellen
    time_label = toga.Label(f"Aktuelle Zeit: {current_time}", style=Pack(padding=10))
    clock_in_button = toga.Button('Kommen', style=Pack(padding=10))
    clock_in_button.on_press = lambda widget: clock_in(widget, vorname, table)
    clock_out_button = toga.Button('Gehen', style=Pack(padding=10))
    clock_out_button.on_press = lambda widget: clock_out(widget, vorname, table)

    # Tabelle erstellen
    table = toga.Table(
        headings=['Vorname', 'Nachname', 'Datum', 'Uhrzeit', 'Ein/Aus'], style=Pack(flex=1)
    )

    # Box erstellen und Komponenten hinzufügen
    button_box = toga.Box(children=[clock_in_button, clock_out_button], style=Pack(direction=ROW, padding=10))
    box = toga.Box(children=[greeting_label, time_label, button_box, table],
                style=Pack(direction=COLUMN, alignment=CENTER, padding=10))

    # Inhalte des Hauptfensters aktualisieren
    return box