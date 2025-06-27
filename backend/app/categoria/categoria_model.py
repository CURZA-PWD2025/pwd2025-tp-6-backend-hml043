from database import DB

class CategoriaModel:

    def __init__(self, id:int = 0, nombre:str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    @staticmethod
    def deserializar(data:dict) -> "CategoriaModel":
        return CategoriaModel(
            id = data.get("id", 0), 
            nombre = data.get("nombre", "")
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM CATEGORIAS"
        result = DB.read(sql)
        return result

    def get_one(self) -> dict:
        sql = "SELECT * FROM CATEGORIAS WHERE id=%s"
        params = (self.id,)
        result = DB.read(sql, params)
        return result

    def create(self) -> int | bool:
        sql = "INSERT INTO CATEGORIAS (nombre) VALUES (%s)"
        params = (self.nombre,)
        return DB.write(sql, params)

    def update(self) -> int | bool:
        sql = "UPDATE CATEGORIAS SET nombre=%s WHERE id=%s"
        params = (self.nombre, self.id)
        return DB.write(sql, params)

    def delete(self) -> int | bool:
        sql = "DELETE FROM CATEGORIAS WHERE id=%s"
        params = (self.id,)
        return DB.write(sql, params)
