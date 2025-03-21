import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL,
    address TEXT NOT NULL
)
""")
conn.commit()
# Insertar usuarios iniciales
initial_users = [
    ("Juan", "3001234567", "juan@mail.com", "Bucaramanga", "Calle 10 #5-20"),
    ("Maria", "3019876543", "maria@mail.com", "Bucaramanga", "Carrera 15 #8-30"),
    ("Carlos", "3025556667", "carlos@mail.com", "Bucaramanga", "Avenida 27 #12-45"),
    ("Ana", "3031112223", "ana@mail.com", "Bucaramanga", "Calle 45 #20-10"),
    ("Luis", "3044445556", "luis@mail.com", "Bucaramanga", "Carrera 9 #7-25"),
    ("Sofia", "3057778889", "sofia@mail.com", "Bucaramanga", "Diagonal 33 #18-50")
]

cursor.executemany("""
INSERT INTO users (name, phone, email, city, address) 
SELECT ?, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM users WHERE name=?)
""", [(u[0], u[1], u[2], u[3], u[4], u[0]) for u in initial_users])
conn.commit()
# Funciones CRUD
def create_user(name, phone, email, city, address):
    cursor.execute("INSERT INTO users (name, phone, email, city, address) VALUES (?, ?, ?, ?, ?)",
                   (name, phone, email, city, address))
    conn.commit()
    print("Usuario creado exitosamente.")

def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

def update_phone(user_id, new_phone):
    cursor.execute("UPDATE users SET phone = ? WHERE id = ?", (new_phone, user_id))
    conn.commit()
    print("Teléfono actualizado.")

def update_email(user_id, new_email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    conn.commit()
    print("Email actualizado.")

def update_user(user_id, phone, email, city, address):
    cursor.execute("UPDATE users SET phone = ?, email = ?, city = ?, address = ? WHERE id = ?",
                   (phone, email, city, address, user_id))
    conn.commit()
    print("Datos actualizados correctamente.")

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("Usuario eliminado.")