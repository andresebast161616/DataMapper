from database.db_connection import get_connection
from models.user import User
from mappers.user_mapper import UserMapper

connection = get_connection()

mapper = UserMapper(connection)

def add_users():
    while True:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(id) FROM users")
        max_id = cursor.fetchone()[0]
        next_id = max_id + 1 if max_id is not None else 1
        
        name = input("Introduce el nombre del usuario: ")
        email = input("Introduce el correo electrónico del usuario: ")
        
        new_user = User(next_id, name, email)
        
        mapper.insert(new_user)
        print(f"Usuario {new_user.name} agregado correctamente con ID {new_user.user_id}.")
        
        another = input("¿Quieres agregar otro usuario? (s/n): ")
        if another.lower() != 's':
            break
        
    show_all_users()

def show_all_users():
    print("\nUsuarios almacenados:")
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Nombre: {row[1]}, Correo: {row[2]}")

add_users()
