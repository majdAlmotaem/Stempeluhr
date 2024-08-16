"""
dieses App ermöglicht den User sich ein und -auszustempeln
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime
import mysql.connector
from .GUI_components.login_window import login
from .GUI_components.main_window import main_window


class stempeluhr(toga.App):

    def startup(self):
        # Verbindung zur MariaDB-Datenbank herstellen
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            charset='utf8mb4',
            database='zeiterfassung'
        )
        self.cursor = self.conn.cursor()
        self.main_window = toga.MainWindow(title='Stempeluhr')
        self.main_window.size = (300, 500)

        login.create_login_ui(self)
         
   

    def register(self,widget):
        pass

    def get_user_info(self, vorname):
        self.cursor.execute('SELECT nachname FROM user WHERE vorname = %s', (vorname,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def clock_in(self, widget):
        vorname = self.vorname_input.value
        current_datetime = datetime.now()
        date = current_datetime.strftime('%Y-%m-%d')
        time = current_datetime.strftime('%H:%M:%S')
        
        # Benutzerinformationen abrufen
        nachname = self.get_user_info(vorname)  # Nur den Nachnamen holen

        if nachname:
            # Benutzer-ID holen
            self.cursor.execute('SELECT id FROM user WHERE vorname = %s AND nachname = %s', (vorname, nachname))
            user_id = self.cursor.fetchone()
            if user_id:
                user_id = user_id[0]
                # Daten in der Datenbank speichern
                self.cursor.execute('INSERT INTO stempel (benutzer_id, datum, uhrzeit, typ) VALUES (%s, %s, %s, %s)',
                                    (user_id, date, time, 'Ein'))
                self.conn.commit()
                self.table.data.append((vorname, nachname, date, time, 'Ein'))
            pass
              
    def clock_out(self, widget):
        vorname = self.vorname_input.value
        current_datetime = datetime.now()
        date = current_datetime.strftime('%Y-%m-%d')
        time = current_datetime.strftime('%H:%M:%S')
        
        # Benutzerinformationen abrufen
        nachname = self.get_user_info(vorname)  # Nur den Nachnamen holen

        if nachname:
            # Benutzer-ID holen
            self.cursor.execute('SELECT id FROM user WHERE vorname = %s AND nachname = %s', (vorname, nachname))
            user_id = self.cursor.fetchone()
            if user_id:
                user_id = user_id[0]
                # Daten in der Datenbank speichern
                self.cursor.execute('INSERT INTO stempel (benutzer_id, datum, uhrzeit, typ) VALUES (%s, %s, %s, %s)',
                                    (user_id, date, time, 'Aus'))
                self.conn.commit()
                self.table.data.append((vorname, nachname, date, time, 'Aus'))
            pass  

    # def load_data(self):
    #     self.cursor.execute('SELECT name, datum, uhrzeit, typ FROM stempel')
    #     for row in self.cursor.fetchall():
    #         self.table.data.append(row)

def main():
    return stempeluhr('Stempeluhr')


if __name__ == '__main__':
    main().main_loop()
