from flask import Blueprint, Request, jsonify
from .marca_controller import MarcaController as Marca

bp_marca = Blueprint("bp_marca", __name__, url_prefix="marcas")

@bp_marca.route("/", methods=["GET"])
def get_all_marcas():
    data = Marca.get_all()
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Marca: no se encontraron datos"}), 204
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_marca.route("/<int:id>", methods=["GET"])
def get_one_marca(id):
    data = Marca.get_one(id)
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Marca: no se encontraron datos"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_marca.route("/", methods=["POST"])
def create_marca():
    data = request.get_json()
    newdata = Marca.create(data)
    try:
        if newdata:
            return jsonify({"message": "Marca: alta exitosa"}), 201
        else:
            return jsonify({"message": "Marca no encontrada"}), 400
    except Exception as err:
        return jsonify({"message": f"Error al crear {err}"}), 500

@bp_marca.route("/<int:id>", methods=["PUT"])
def update_marca(id):
    data = request.get_json()
    newdata = Marca.update(data)
    try:
        if newdata:
            return jsonify({"message": "Marca: modificacion exitosa"}), 201
        else:
            return jsonify({"message": "Marca no encontrada"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al modificar {err}"}), 500

@bp_marca.route("/<int:id>", methods=["DELETE"])
def delete_marca(id):
    data = Marca.delete(id)
    try:
        if data:
            return jsonify({"message": "Marca: baja exitosa"}), 200
        else:
            return jsonify({"message": "Marca no encontrada"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al eliminar {err}"}), 500
