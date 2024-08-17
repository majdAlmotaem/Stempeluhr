"""
dieses App ermöglicht den User sich ein und -auszustempeln
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime
from .GUI_components.login_window import create_login_ui



class stempeluhr(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title='Stempeluhr')
        self.main_window.size = (300, 500)
        
        self.main_window.content= create_login_ui(self.main_window)
        
    
    def get_user_info(self, vorname):
        self.cursor.execute('SELECT nachname FROM user WHERE vorname = %s', (vorname,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    

  
            


    # def load_data(self):
    #     self.cursor.execute('SELECT name, datum, uhrzeit, typ FROM stempel')
    #     for row in self.cursor.fetchall():
    #         self.table.data.append(row)


def main():
    return stempeluhr('Stempeluhr')


if __name__ == '__main__':
    main().main_loop()
