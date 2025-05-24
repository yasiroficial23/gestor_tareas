# Gestor de Tareas

Aplicación web para gestionar tareas personales, desarrollada como parte de la actividad #4 de topicos avanzados de software por: Yasir Garcia, Alejandro Jimenez y Diego Alvarez, utilizando **Arquitectura Hexagonal**, **Código Limpio** y **principios SOLID**.

## Tecnologías
- **Backend**: Flask (Python), SQLite
- **Frontend**: React
- **Base de datos**: SQLite

## Estructura del Proyecto
- `app/domain`: Contiene las entidades (`tarea.py`) y puertos (`puertos.py`) que definen el núcleo del dominio.
- `app/use_cases`: Incluye los casos de uso (`tarea_usecase.py`) para la lógica de negocio.
- `app/adapters/inbound`: Controladores Flask (`controlador.py`) que manejan las solicitudes HTTP.
- `app/adapters/outbound`: Implementación del repositorio con SQLite (`sqlite_repositorio.py`).
- `frontend`: Interfaz de usuario desarrollada con React.

## Instalación
1. **Backend**:
   - Navega al directorio del proyecto:
     ```bash
     cd gestor_tareas

## Crea y activa un entorno virtual:
bash
python -m venv env

env\Scripts\activate  # En Windows, usa esto; en Linux/Mac, usa 'source env/bin/activate'

## Instala las dependencias:
bash
pip install -r requirements.txt

## Ejecuta la aplicación:
bash
python app/main.py

## Frontend:
Navega al directorio del frontend:
bash
cd frontend

## Instala las dependencias:
bash
npm install

## Inicia la aplicación:
bash
npm start

## Accede a la interfaz en http://localhost:3000.
Uso
## Accede a la interfaz en http://localhost:3000.
## Usa el formulario para crear nuevas tareas ingresando un título y una descripción.
## La lista mostrará todas las tareas creadas (puede requerir recargar manualmente la página).
## Principios Aplicados
## Clean Code:
Uso de nombres descriptivos (ej. Tarea, CrearTareaUseCase).
Funciones con una sola responsabilidad (ej. crear() en SqliteRepositorio).
## SOLID:
S (Single Responsibility): Cada clase tiene una sola responsabilidad (ej. CrearTareaUseCase solo crea tareas).
D (Dependency Inversion): Los casos de uso dependen de la interfaz RepositorioTareas en lugar de una implementación concreta.
## Refactorización:
Ejemplo en controlador.py, donde se renombró la variable data a tarea_data para mayor claridad (ver comentario en el código).
## Repositorio
https://github.com/yasiroficial23/gestor_tareas.git
## Capturas
Formulario de creación: ![image](https://github.com/user-attachments/assets/c9d2a94c-4a97-4f06-b299-2dd66ae78d6c)

Lista de tareas: ![image](https://github.com/user-attachments/assets/49d4a8b2-bafe-4f4b-b935-970226b25063)

## Equipo
Yasir Garcia,
Alejandro Jimenez,
Diego Alvarez
