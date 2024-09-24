"""
dieses App ermöglicht den User sich ein und -auszustempeln
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from .functions.create_starter_window import create_starter_window
from .classes.state import state



class stempeluhr(toga.App):

    def startup(self):
        # Main Window erstellen
        self.main_window = toga.MainWindow(title='Stempeluhr')
        self.main_window.size = (300, 500)
        
        # Main Window im Singleton speichern
        state.main_window = self.main_window
        
        # Starter Window erzeugen
        self.main_window.content = create_starter_window()
        self.main_window.show()


def main():
    return stempeluhr('Stempeluhr')


if __name__ == '__main__':
    main().main_loop()
