"""
dieses App ermöglicht den User sich ein und -auszustempeln
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime


class stempeluhr(toga.App):

    def startup(self):
        # Hauptfenster erstellen
        self.main_window = toga.MainWindow(title=self.name)

        # Komponenten erstellen
        name_label = toga.Label(
            "Geben Sie Ihren Name ein: ", style=Pack(padding=(0,5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.time_label = toga.Label("Aktuelle Zeit: --:--", style=Pack(padding=10))
        self.in_out_label = toga.Label("Stempel: --", style=Pack(padding=10))
        self.clock_in_button = toga.Button('Kommen', on_press=self.clock_in, style=Pack(padding=10))
        self.clock_out_button = toga.Button('Gehen', on_press=self.clock_out, style=Pack(padding=10))

        # Box erstellen und Komponenten hinzufügen
        name_box = toga.Box(children=[name_label, self.name_input], style=Pack(direction=ROW, padding=5))
        button_box = toga.Box(children=[self.clock_in_button, self.clock_out_button], style=Pack(direction=ROW, padding=10))
        box = toga.Box(children=[self.time_label, name_box, self.in_out_label, button_box],
                        style=Pack(direction=COLUMN, alignment=CENTER, padding=10))

        # Box zum Hauptfenster hinzufügen
        
        self.main_window.content = box
        self.main_window.show()

        # Uhrzeit regelmäßig aktualisieren
        self.update_time()


    def update_time(self):
        current_time = datetime.now().strftime("%H:%M")
        self.time_label.text = f"Aktuelle Zeit: {current_time}"
        

    def clock_in(self, widget):
        self.in_out_label.text = f"Stempel: {self.name_input.value} hat um {datetime.now().strftime('%H:%M')} Uhr eingestempelt"
        self.in_out_label.refresh()

    def clock_out(self, widget):
        self.in_out_label.text = f"Stempel: {self.name_input.value} hat um {datetime.now().strftime('%H:%M')} Uhr ausgestempelt"
        self.in_out_label.refresh()


def main():
    return stempeluhr('Stempeluhr')


if __name__ == '__main__':
    main().main_loop()
