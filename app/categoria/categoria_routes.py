from flask import Blueprint, Request, jsonify
from .categoria_controller import CategoriaController

bp_categoria = Blueprint("bp_categoria", __name__, url_prefix="categorias")

@bp_categoria.route("/", methods=["GET"])
def get_all_categorias():
    data = CategoriaController.get_all()
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Categoria: no se encontraron datos"}), 204
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_categoria.route("/<int:id>", methods=["GET"])
def get_one_categoria(id):
    data = CategoriaController.get_one(id)
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Categoria: no se encontraron datos"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_categoria.route("/", methods=["POST"])
def create_categoria():
    data = request.get_json()
    new_data = CategoriaController.create(data)
    try:
        if new_data:
            return jsonify({"message": "Categoria: alta exitosa"}), 201
        else:
            return jsonify({"message": "Categoria no encontrada"}), 400
    except Exception as err:
        return jsonify({"message": f"Error al crear {err}"}), 500

@bp_categoria.route("/<int:id>", methods=["PUT"])
def update_categoria(id):
    data = request.get_json()
    new_data = CategoriaController.update(data)
    try:
        if new_data:
            return jsonify({"message": "Categoria: modificacion exitosa"}), 201
        else:
            return jsonify({"message": "Categoria no encontrada"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al modificar {err}"}), 500

@bp_categoria.route("/<int:id>", methods=["DELETE"])
def delete_categoria(id):
    data = CategoriaController.delete(id)
    try:
        if data:
            return jsonify({"message": "Categoria: baja exitosa"}), 200
        else:
            return jsonify({"message": "Categoria no encontrada"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al eliminar {err}"}), 500
