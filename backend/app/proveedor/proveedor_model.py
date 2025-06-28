from database import DB

class ProveedorModel:

    def __init__(self, id:int = 0, nombre:str = "", telefono:int = 0, direccion:str = "", email:str = ""):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self) -> dict:  
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    @staticmethod
    def deserializar(data:dict) -> "ProveedorModel":
        return ProveedorModel(
            id = data.get("id", 0),
            nombre = data.get("nombre", ""),
            telefono = data.get("telefono", 0),
            direccion = data.get("direccion", ""),
            email = data.get("email", "")
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM PROVEEDORES"
        result = DB.read(sql)
        return result

    def get_one(self) -> dict:
        sql = "SELECT * FROM PROVEEDORES WHERE id=%s"
        params = (self.id,)
        result = DB.read(sql, params)
        return result

    def create(self) -> int | bool:
        sql = "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)"
        params = (self.nombre, self.telefono, self.direccion, self.email)
        return DB.write(sql, params)

    def update(self) -> int | bool:
        sql = "UPDATE PROVEEDORES SET nombre=%s, telefono=%s, direccion=%s, email=%s WHERE id=%s"
        params = params = (self.nombre, self.telefono, self.direccion, self.email, self.id)
        return DB.write(sql, params)

    def delete(self) -> int | bool:
        sql = "DELETE FROM PROVEEDORES WHERE id=%s"
        params = (self.id,)
        return DB.write(sql, params)
