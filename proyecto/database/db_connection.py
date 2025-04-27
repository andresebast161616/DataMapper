# /database/db_connection.py
import sqlite3

def get_connection():
    # Crea la conexión a la base de datos en memoria
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Crear tabla de usuarios
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    connection.commit()

    return connection
