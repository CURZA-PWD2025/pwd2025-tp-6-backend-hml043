from database import DB

class CategoriaModel:

    def __init__(self, id:int = 0, descripcion:str = ""):
        self.id = id
        self.descripcion = descripcion

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data:dict) -> "CategoriaModel":
        return CategoriaModel(
            id = data.get("id", 0), 
            descripcion = data.get("descripcion", "")
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM categorias"
        result = DB.read(sql)
        return result

    def get_one(self) -> dict:
        sql = "SELECT * FROM categorias WHERE id=%s"
        params = (self.id,)
        result = DB.read(sql, params)
        return result

    def create(self) -> int | bool:
        sql = "INSERT INTO categorias (descripcion) VALUES (%s)"
        params = (self.descripcion,)
        return DB.write(sql, params)

    def update(self) -> int | bool:
        sql = "UPDATE categorias SET descripcion=%s WHERE id=%s"
        params = (self.descripcion, self.id)
        return DB.write(sql, params)

    def delete(self) -> int | bool:
        sql = "DELETE FROM categorias WHERE id=%s"
        params = (self.id,)
        return DB.write(sql, params)
