import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime

class main_window(toga.MainWindow):
    def create_main_ui(self):
            self.main_window.title = 'Zeiterfassung'
            self.main_window.size = (400, 600)  # Fenstergröße anpassen
            
            # Begrüßung erstellen und zentrieren
            greeting_label = toga.Label(
                f"Willkommen, {self.vorname_input.value}!",
                style=Pack(padding=10, text_align="center")
            )
            current_time = datetime.now().strftime("%H:%M")
            # Weitere Komponenten erstellen
            self.time_label = toga.Label(f"Aktuelle Zeit: {current_time}", style=Pack(padding=10))
            self.clock_in_button = toga.Button('Kommen', on_press=self.clock_in, style=Pack(padding=10))
            self.clock_out_button = toga.Button('Gehen', on_press=self.clock_out, style=Pack(padding=10))

            # Tabelle erstellen
            self.table = toga.Table(
                headings=['Vorname', 'Nachname', 'Datum', 'Uhrzeit', 'Ein/Aus'], style=Pack(flex=1)
            )

            # Box erstellen und Komponenten hinzufügen
            button_box = toga.Box(children=[self.clock_in_button, self.clock_out_button], style=Pack(direction=ROW, padding=10))
            box = toga.Box(children=[greeting_label, self.time_label, button_box, self.table],
                        style=Pack(direction=COLUMN, alignment=CENTER, padding=10))

            # Inhalte des Hauptfensters aktualisieren
            self.main_window.content = box