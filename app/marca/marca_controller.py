from .marca_model import MarcaModel as Marca

class MarcaController:

    @staticmethod
    def get_all():
        return Marca.get_all()

    @staticmethod
    def get_one(id: int):
        return Marca(id=id).get_one()

    @staticmethod
    def create(data: dict):
        marca = Marca(descripcion=data['descripcion'])
        return marca.create()

    @staticmethod
    def update(data: dict):
        #marca = Marca(id=data['id'], descripcion=data['descripcion'])
        return mMarca.deserializar(data).update()

    @staticmethod
    def delete(id: int):
        return Marca(id=id).delete()
