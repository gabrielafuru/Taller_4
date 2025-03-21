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