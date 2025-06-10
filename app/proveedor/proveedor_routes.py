from flask import Blueprint, Request, jsonify
from .proveedor_controller import ProveedorController as Proveedor

bp_proveedor = Blueprint("bp_proveedor", __name__, url_prefix="proveedores")

@bp_proveedor.route("/", methods=["GET"])
def get_all_proveedores():
    data = Proveedor.get_all()
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Proveedor: no se encontraron datos"}), 204
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_proveedor.route("/<int:id>", methods=["GET"])
def get_one_proveedor(id):
    data = Proveedor.get_one(id)
    try:
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "Proveedor: no se encontraron datos"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al listar {err}"}), 500

@bp_proveedor.route("/", methods=["POST"])
def create_proveedor():
    data = request.get_json()
    newdata = Proveedor.create(data)
    try:
        if newdata:
            return jsonify({"message": "Proveedor: alta exitosa"}), 201
        else:
            return jsonify({"message": "Proveedor no encontrado"}), 400
    except Exception as err:
        return jsonify({"message": f"Error al crear {err}"}), 500

@bp_proveedor.route("/<int:id>", methods=["PUT"])
def update_proveedor(id):
    data = request.get_json()
    newdata = Proveedor.update(data)
    try:
        if newdata:
            return jsonify({"message": "Proveedor: modificacion exitosa"}), 201
        else:
            return jsonify({"message": "Proveedor no encontrado"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al modificar {err}"}), 500

@bp_proveedor.route("/<int:id>", methods=["DELETE"])
def delete_proveedor(id):
    data = Proveedor.delete(id)
    try:
        if data:
            return jsonify({"message": "Proveedor: baja exitosa"}), 200
        else:
            return jsonify({"message": "Proveedor no encontrado"}), 404
    except Exception as err:
        return jsonify({"message": f"Error al eliminar {err}"}), 500
