from .proveedor_model import ProveedorModel as Proveedor

class ProveedorController:

    @staticmethod
    def get_all():
        return Proveedor.get_all()

    @staticmethod
    def get_one(id: int):
        return Proveedor(id=id).get_one()

    @staticmethod
    def create(data: dict):
        proveedor = Proveedor(nombre=data['nombre'], telefono=data['telefono'], direccion=data['direccion'], email=data['email'])
        return proveedor.create()

    @staticmethod
    def update(data: dict):
        #proveedor = ProveedorModel(id=data['id'], nombre=data['nombre'], ...)
        return Proveedor.deserializar(data).update()

    @staticmethod
    def delete(id: int):
        return Proveedor(id=id).delete()
