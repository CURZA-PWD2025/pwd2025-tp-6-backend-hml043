from flask import Blueprint, request, jsonify
from .articulo_controller import ArticuloController as Articulo

bp_articulo = Blueprint("bp_articulo", __name__, url_prefix="articulos")

@bp_articulo.route("/", methods=["GET"])
def get_all_articulos():
    data = Articulo.get_all()
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Articulo: no se encontraron datos"}), 204
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_articulo.route("/<int:id>", methods=["GET"])
def get_one_articulo(id):
    data = Articulo.get_one(id)
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Articulo: no se encontraron datos"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_articulo.route("/", methods=["POST"])
def create_articulo():
    data = request.get_json()
    newdata = Articulo.create(data)
    try:
        if newdata:
            return jsonify({"message": "Articulo: alta exitosa"}), 201
        else:
            return jsonify({"message": "Articulo no encontrado"}), 400
    except Exception as err:
        return jsonify({"message": f"Error al crear {err}"}), 500

@bp_articulo.route("/<int:id>", methods=["PUT"])
def update_articulo(id):
    data = request.get_json()
    data['id'] = id
    newdata = Articulo.update(data)
    try:
        if newdata:
            return jsonify({"message": "Articulo: modificacion exitosa"}), 201
        else:
            return jsonify({"message": "Articulo no encontrado"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al modificar {err}"}), 500

@bp_articulo.route("/<int:id>", methods=["DELETE"])
def delete_articulo(id):
    data = Articulo.delete(id)
    try:
        if data:
            return jsonify({"message": "Articulo: baja exitosa"}), 200
        else:
            return jsonify({"message": "Articulo no encontrado"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al eliminar {err}"}), 500
