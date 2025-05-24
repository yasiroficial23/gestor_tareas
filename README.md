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
