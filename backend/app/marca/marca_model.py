from database import DB

class MarcaModel:

    def __init__(self, id:int = 0, nombre:str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    @staticmethod
    def deserializar(data:dict) -> "MarcaModel":
        return MarcaModel(
            id = data.get("id", 0), 
            nombre = data.get("nombre", "")
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM MARCAS"
        result = DB.read(sql)
        return result

    def get_one(self) -> dict:
        sql = "SELECT * FROM MARCAS WHERE id=%s"
        params = (self.id,)
        result = DB.read(sql, params)
        return result

    def create(self) -> int | bool:
        sql = "INSERT INTO MARCAS (nombre) VALUES (%s)"
        params = (self.nombre,)
        return DB.write(sql, params)

    def update(self) -> int | bool:
        sql = "UPDATE MARCAS SET nombre=%s WHERE id=%s"
        params = (self.nombre, self.id)
        #print('debug update model')
        #print(params)
        #print('debug update model')
        return DB.write(sql, params)

    def delete(self) -> int | bool:
        sql = "DELETE FROM MARCAS WHERE id=%s"
        params = (self.id,)
        return DB.write(sql, params)
