from flask import Blueprint, request, jsonify
from app.domain.tarea import Tarea

def crear_controlador(crear_uc, listar_uc):
    tareas_bp = Blueprint("tareas", __name__)

    @tareas_bp.route("/tareas", methods=["POST"])
    def crear_tarea():
        data = request.json
        tarea = Tarea(id=None, titulo=data["titulo"], descripcion=data.get("descripcion", ""))
        tarea_creada = crear_uc.ejecutar(tarea)
        return jsonify({
            "id": tarea_creada.id,
            "titulo": tarea_creada.titulo,
            "descripcion": tarea_creada.descripcion,
            "completada": tarea_creada.completada
        }), 201

    @tareas_bp.route("/tareas", methods=["GET"])
    def listar_tareas():
        tareas = listar_uc.ejecutar()
        return jsonify([{
            "id": t.id,
            "titulo": t.titulo,
            "descripcion": t.descripcion,
            "completada": t.completada
        } for t in tareas])

    return tareas_bp
