from .marca_model import MarcaModel as Marca

class MarcaController:

    @staticmethod
    def get_all():
        return Marca.get_all()

    @staticmethod
    def get_one(id:int):
        return Marca(id=id).get_one()

    @staticmethod
    def create(data:dict):
        marca = Marca(nombre=data['nombre'])
        return marca.create()

    @staticmethod
    def update(data:dict):
        #print('debug update controler')
        #print(data)
        #print('debug update controler')
        #marca = Marca(id=data['id'], nombre=data['nombre']) #otra forma
        return Marca.deserializar(data).update()

    @staticmethod
    def delete(id:int):
        return Marca(id=id).delete()
