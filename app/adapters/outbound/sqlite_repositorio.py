import sqlite3
from app.domain.puertos import RepositorioTareas
from app.domain.tarea import Tarea

class SqliteRepositorio(RepositorioTareas):
    def __init__(self, db_path="database.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                completada BOOLEAN DEFAULT 0
            )
        ''')
        self.conn.commit()

    def crear(self, tarea):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO tareas (titulo, descripcion, completada)
            VALUES (?, ?, ?)
        ''', (tarea.titulo, tarea.descripcion, tarea.completada))
        self.conn.commit()
        tarea.id = cursor.lastrowid
        return tarea

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, titulo, descripcion, completada FROM tareas')
        filas = cursor.fetchall()
        return [Tarea(*fila) for fila in filas]
