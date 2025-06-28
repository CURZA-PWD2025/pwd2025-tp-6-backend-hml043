from  .articulo_model            import ArticuloModel   as Articulo
from ..categoria.categoria_model import CategoriaModel  as Categoria
from ..proveedor.proveedor_model import ProveedorModel  as Proveedor
from ..marca.marca_model         import MarcaModel      as Marca

from ..proveedor.proveedor_controller   import ProveedorController
from ..marca.marca_controller           import MarcaController

class ArticuloController:


    @staticmethod
    def _anexar_datos(data):  # metodo privado para completar el diccionario del artículo con los objetos de marca, proveedor y categoria
        #print('debug...')
        #print(data)
        #print('debug...')
        if not data:
            return None
        marca       = None
        proveedor   = None
        categorias  = []        
        if data['marca_id']:
            marca = MarcaController.get_one(data['marca_id'])
        if data['proveedor_id']:
            proveedor = ProveedorController.get_one(data['proveedor_id'])
        db_data = ArticuloController._get_group_articulo_categoria(data['id'])        
        #print('debug art_cat...')
        #print(result_list)
        #print('debug art_cat...')
        if db_data:
            categorias  = [Categoria(**c).serializar() for c in db_data] if db_data else []  #Convertir objetos Categoria a lista de diccionarios
        articulo = Articulo(                                    # crear instancia de un articulo con los objetos relacionados
            id              = data['id'],
            descripcion     = data['descripcion'],
            precio          = data['precio'],
            stock           = data['stock'],
            marca_id        = data['marca_id'],         # mantener id marca
            proveedor_id    = data['proveedor_id']      # mantener id proveedor            
            #fecha_alta      = data['fecha_alta'],
        ).serializar()
        articulo['marca']       = marca                 # los argumentos marca y proveedor se pasan como objetos marca/proveedor
        articulo['proveedor']   = proveedor
        articulo['categorias']  = categorias            # categorias se pasa como una lista de objetos categoria        
        return articulo

    @staticmethod
    def get_all():
        db_data = Articulo.get_all()
        #if not db_data:
        #    return []
        articulos = [ArticuloController._anexar_datos(a) for a in db_data] if db_data else []   #completar cada artículo y convertirlo a diccionario para la salida API        
        return articulos
        """
            articulo                = Articulo(id=p['id'], descripcion=p['descripcion'], precio=p['precio'], stock=p['stock'], marca_id=p['marca_id'], proveedor_id=p['proveedor_id']).to_dict()
            articulo['marca']       = Marca(id=p['marca_id']).get_one()
            articulo['proveedor']   = Proveedor(id=p['proveedor_id']).get_one()
            articulo['categorias']  = Categorias(id=p['proveedor_id']).get_one()
            articulos.append(articulo)
        """
        #return Articulo.get_all()

    @staticmethod
    def get_one(id:int):
        db_data = Articulo(id=id).get_one()
        #print('debug one...')
        #print(db_data)
        #print('debug one...')
        articulo = ArticuloController._anexar_datos(db_data[0]) if db_data else {}
        return articulo

    @staticmethod
    def create(data:dict):
        #print('debug create...')
        #print(data)
        #print('debug create...')
        #categorias_id = data['categorias'] ## debe ser similar a [1,5,13] lista de ids de categorias
        #categorias  = []
        #for id in categorias_id:
        #    categorias.append(Categoria(id=id))
        #data['categorias']  = categorias
        #data['proveedor']   = Proveedor(id=data['proveedor_id'])
        #data['marca']       = Marca(id=data['marca_id'])
        articulo = Articulo(descripcion=data['descripcion'], precio=float(data['precio']), stock=int(data['stock']),
                                marca_id=int(data['marca_id']), proveedor_id=int(data['proveedor_id']))
                                #proveedor=data['proveedor'], marca=data['marca'], categorias=data['categorias']
        #print(articulo)
        new_id = articulo.create()
        if new_id > 0 and data['categorias']:
            for c in data['categorias']: ArticuloController._insert_articulo_categoria(int(new_id), int(c))
        return new_id

    @staticmethod
    def update(data:dict):
        #categorias_id = data['categorias'] ## debe ser similar a [1,5,13] lista de ids de categorias
        #categorias  = []
        #for id in categorias_id:
        #    categorias.append(Categoria(id=id))
        #data['categorias']  = categorias
        #data['proveedor']   = Proveedor(id=data['proveedor_id'])
        #data['marca']       = Marca(id=data['marca_id'])
        #del data['proveedor_id']
        #del data['marca_id']
        #print(data)
        articulo = Articulo.deserializar(data).update()
        #print('debug update...')
        #print(articulo)
        #print('debug update...')
        if articulo:
            if data['categorias']:
                db_data = ArticuloController._get_group_articulo_categoria(int(data['id'])) #recuperar para comparar y obtener altas y bajas puras
                if db_data:                                     #existen categorias para el articulo
                    lst_ids = [int(d['id']) for d in db_data]   #genero una lista con id de las categorias existntes
                    lst_del = [x for x in lst_ids if x not in data['categorias']]    #genero una lista con id de las categorias a quitar
                    lst_ins = [x for x in data['categorias'] if x not in lst_ids]    #genero una lista con id de las categorias a insertar
                    #print('debug upd cat...')
                    #print(db_data)
                    #print(lst_ids)
                    #print(lst_del)
                    #print(lst_ins)
                    #print('debug upd cat...')
                    for c in lst_del: ArticuloController._delete_articulo_categoria(int(data['id']), int(c))
                    for c in lst_ins: ArticuloController._insert_articulo_categoria(int(data['id']), int(c))
                else:
                    for c in data['categorias']: ArticuloController._insert_articulo_categoria(int(data['id']), int(c))
            else:
                ArticuloController._delete_articulo_categoria(int(data['id']),)   # si no se informan categorias quitar las existentes
        #print(articulo)
        return articulo

    @staticmethod
    def delete(id:int):
        ArticuloController._delete_articulo_categoria(int(id),)
        return Articulo(id=id).delete()

    """
    especifico para Articulos + Categorias
    """
    @staticmethod
    def _get_group_articulo_categoria(id:int):       # obtiene las categorías asociadas a un artículo por su ID
        return Articulo(id=id).get_group_articulo_categoria()

    @staticmethod
    def _insert_articulo_categoria(art_id:int, cat_id:int):    # asocia un articulo con una categoria
        return Articulo().insert_articulo_categoria(art_id, cat_id)

    @staticmethod
    def _delete_articulo_categoria(art_id:int, cat_id:int=None): # elimina categorias de un articulo, si categoria_id es 'None' elimina todas
        return Articulo().delete_articulo_categoria(art_id, cat_id)