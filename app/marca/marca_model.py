from database import DB

class MarcaModel:

    def __init__(self, id:int = 0, descripcion:str = ""):
        self.id = id
        self.descripcion = descripcion

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data:dict) -> "MarcaModel":
        return MarcaModel(
            id = data.get("id", 0), 
            descripcion = data.get("descripcion", "")
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM marcas"
        result = DB.read(sql)
        return result

    def get_one(self) -> dict:
        sql = "SELECT * FROM marcas WHERE id=%s"
        params = (self.id,)
        result = DB.read(sql, params)
        return result

    def create(self) -> int | bool:
        sql = "INSERT INTO marcas (descripcion) VALUES (%s)"
        params = (self.descripcion,)
        return DB.write(sql, params)

    def update(self) -> int | bool:
        sql = "UPDATE marcas SET descripcion=%s WHERE id=%s"
        params = (self.descripcion, self.id)
        return DB.write(sql, params)

    def delete(self) -> int | bool:
        sql = "DELETE FROM marcas WHERE id=%s"
        params = (self.id,)
        return DB.write(sql, params)
