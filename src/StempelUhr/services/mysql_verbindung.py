import mysql.connector

def mysql_verbindung():
    # Verbindung zur MariaDB-Datenbank herstellen
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        charset='utf8mb4',
        database='zeiterfassung'
    )
    cursor = conn.cursor()
    return conn, cursor