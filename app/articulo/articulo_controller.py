from  .articulo_model            import ArticuloModel   as Articulo
from ..categoria.categoria_model import CategoriaModel  as Categoria
from ..proveedor.proveedor_model import ProveedorModel  as Proveedor
from ..marca.marca_model         import MarcaModel      as Marca

class ArticuloController:

    @staticmethod
    def get_all():
        return Articulo.get_all()

    @staticmethod
    def get_one(id: int):
        return Articulo(id=id).get_one()

    @staticmethod
    def create(data: dict):
        categorias_id = data['categorias'] ## es igual a {1,5,13} lista de ids de categorias
        categorias  = []
        for id in categorias_id:
            categorias.append(Categoria(id=id))
        data['categorias']  = categorias
        data['proveedor']   = Proveedor(id=data['proveedor_id'])
        data['marca']       = Marca(id=data['marca_id'])
        articulo = Articulo(descripcion=data['descripcion'], precio=float(data['precio']), stock=int(data['stock']),
                                proveedor=data['proveedor'], marca=data['marca'], categorias=data['categorias'])
                                #marca_id=data['marca_id'], proveedor_id=data['proveedor_id']
        #print(articulo)
        return articulo.create()

    @staticmethod
    def update(data: dict):
        categorias_id = data['categorias'] ## es igual a {1,5,13} lista de ids de categorias
        categorias  = []
        for id in categorias_id:
            categorias.append(Categoria(id=id))
        data['categorias']  = categorias
        data['proveedor']   = Proveedor(id=data['proveedor_id'])
        data['marca']       = Marca(id=data['marca_id'])
        del data['proveedor_id']
        del data['marca_id']
        #print(data)
        articulo = Articulo.deserializar(data).update()
        #print(articulo)
        return articulo

    @staticmethod
    def delete(id: int):
        return ArticuloModel(id=id).delete()
