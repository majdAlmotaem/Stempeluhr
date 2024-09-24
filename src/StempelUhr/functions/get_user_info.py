from .mysql_verbindung import mysql_verbindung
   


def get_user_info(vorname):
    _, cursor = mysql_verbindung()
    cursor.execute('SELECT nachname FROM user WHERE vorname = %s', (vorname,))
    result = cursor.fetchone()
    return result[0] if result else None
