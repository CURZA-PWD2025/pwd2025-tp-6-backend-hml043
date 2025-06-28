from .categoria_model import CategoriaModel as Categoria

class CategoriaController:

    @staticmethod
    def get_all():
        return Categoria.get_all()

    @staticmethod
    def get_one(id: int):
        return Categoria(id=id).get_one()

    @staticmethod
    def create(data: dict):
        categoria = Categoria(nombre=data['nombre'])
        return categoria.create()

    @staticmethod
    def update(data: dict):
        #categoria = Categoria(id=data['id'], descripcion=data['descripcion'])
        return Categoria.deserializar(data).update()

    @staticmethod
    def delete(id: int):
        return Categoria(id=id).delete()
