from database import DB

class ArticuloModel:

    def __init__(self, id:int = 0, descripcion="", precio:float = 0.0, stock:int = 0, marca_id:int = None, proveedor_id:int = None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id  
        self.proveedor_id = proveedor_id 
        self.marca = None
        self.proveedor = None
        self.categorias = []

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id
        }        

    @staticmethod
    def deserializar(data) -> "ArticuloModel":
        return ArticuloModel(
            id          = data.get("id", 0),
            descripcion = data.get("descripcion", ""),
            precio      = data.get("precio", 0.0),
            stock       = data.get("stock", 0),
            marca_id    = data.get("marca_id", 0),
            proveedor_id = data.get("proveedor_id", 0)
        )
    
    @staticmethod
    def get_all() -> list[dict]:
        qry = "SELECT * FROM ARTICULOS"
        result = DB.read(qry)
        return result

    def get_one(self) -> dict:
        qry = "SELECT * FROM ARTICULOS WHERE id=%s"
        params = (self.id,)
        result = DB.read(qry, params)
        return result

    def create(self) -> int | bool:
        qry = "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)"
        params = (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
        new_id = DB.write(qry, params)
        #if new_id > 0 and self.categorias:
        #    for c in self.categorias: self.insert_articulo_categoria(new_id, int(c))
        return new_id

    def update(self) -> int | bool:
        qry = "UPDATE ARTICULOS SET descripcion=%s, precio=%s, stock=%s, marca_id=%s, proveedor_id=%s WHERE id=%s"
        params = (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id, self.id)
        cnt_row = DB.write(qry, params)
        #if cnt_row > 0 and self.categorias:
        #    for c in self.categorias: self.insert_articulo_categoria(self.id, int(c))
        return cnt_row

    def delete(self) -> int | bool:
        qry = "DELETE FROM ARTICULOS WHERE id=%s"
        params = (self.id,)
        return DB.write(qry, params)

    def get_group_articulo_categoria(self):       # obtiene las categorías asociadas a un artículo por su ID
        qry = """
                SELECT c.id, c.nombre
                FROM CATEGORIAS c
                JOIN ARTICULOS_CATEGORIAS ac ON c.id=ac.categoria_id
                WHERE ac.articulo_id=%s
            """
        params = (self.id,)
        result = DB.read(qry, params)
        return result

    @staticmethod
    def insert_articulo_categoria(id:int, cat_id:int):    # asocia un articulo con una categoria
        qry = "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)"
        params = (id, cat_id)
        return DB.write(qry, params)

    @staticmethod
    def delete_articulo_categoria(id:int, cat_id:int=None): # elimina categorias de un articulo, si categoria_id es 'None' elimina todas
        qry = "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id=%s"+(" AND categoria_id=%s" if cat_id else "")
        if cat_id:
            #qry = "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id=%s AND categoria_id=%s"
            params = (id, cat_id)
        else:
            #qry = "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id=%s"
            params = (id,)        
        return DB.write(qry, params)
