from database import DB

class ArticuloModel:

    def __init__(self, id:int = 0, descripcion="", precio:float = 0.0, stock:int = 0, marca_id:int = None, proveedor_id:int = None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id  
        self.proveedor_id = proveedor_id 
        self._marca = None  
        self._proveedor = None  
        self._categorias = []

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
            id = data.get("id", 0),
            descripcion = data.get("descripcion", ""),
            precio = data.get("precio", 0.0),
            stock = data.get("stock", 0),
            marca_id = data.get("marca_id", 0),
            proveedor_id = data.get("proveedor_id", 0)
        )
    
    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM articulos"
        result = DB.read(sql)
        return result

    def get_one(self) -> dict:
        sql = "SELECT * FROM articulos WHERE id=%s"
        params = (self.id,)
        result = DB.read(sql, params)
        return result

    def create(self) -> int | bool:
        sql = "INSERT INTO articulos (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s)"
        params = (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
        return DB.write(sql, params)

    def update(self) -> int | bool:
        sql = "UPDATE articulos SET descripcion=%s, precio=%s, stock=%s, marca_id=%s, proveedor_id=%s WHERE id=%s"
        params = (self.nombre, self.id)
        return DB.write(sql, params)

    def delete(self) -> int | bool:
        sql = "DELETE FROM articulos WHERE id=%s"
        params = (self.id,)
        return DB.write(sql, params)
