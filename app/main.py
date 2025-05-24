import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS

from app.use_cases.tarea_usecase import CrearTareaUseCase, ListarTareasUseCase
from app.adapters.outbound.sqlite_repositorio import SqliteRepositorio
from app.adapters.inbound.controlador import crear_controlador

def crear_app():
    app = Flask(__name__)
    CORS(app)  # Permite llamadas desde el frontend

    # Repositorio e inyección de dependencias
    repositorio = SqliteRepositorio()
    crear_uc = CrearTareaUseCase(repositorio)
    listar_uc = ListarTareasUseCase(repositorio)

    # Registrar rutas
    tareas_bp = crear_controlador(crear_uc, listar_uc)
    app.register_blueprint(tareas_bp)

    return app

if __name__ == "__main__":
    app = crear_app()
    app.run(debug=True)