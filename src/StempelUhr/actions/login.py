 

def login(self, widget):
    vorname = self.vorname_input.value
    # Überprüfen, ob der Benutzer existiert
    self.cursor.execute('SELECT vorname FROM user WHERE vorname = %s', (vorname,))
    user = self.cursor.fetchone()
    
    if user and user[0] == vorname:
        main_window.create_main_ui(self)
    else:
        pass