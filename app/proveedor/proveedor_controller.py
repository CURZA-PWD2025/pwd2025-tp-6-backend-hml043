from .proveedor_model import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id: int):
        return ProveedorModel(id=id).get_one()

    @staticmethod
    def create(data: dict):
        proveedor = ProveedorModel(nombre=data['nombre'], telefono=data['telefono'], direccion=data['direccion'], email=data['email'])
        return proveedor.create()

    @staticmethod
    def update(data: dict):
        #proveedor = ProveedorModel(id=data['id'], nombre=data['nombre'], ...)
        return ProveedorModel.deserializar(data).update()

    @staticmethod
    def delete(id: int):
        return ProveedorModel(id=id).delete()
