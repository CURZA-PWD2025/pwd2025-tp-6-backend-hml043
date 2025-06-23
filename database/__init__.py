import os
import mysql.connector

from mysql.connector import Error
from mysql.connector.constants import ClientFlag
from dotenv import load_dotenv

load_dotenv()

""" NOTA
https://stackoverflow.com/questions/50796603/do-you-need-to-update-the-data-when-it-doesnt-change
https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html

Para sentencias UPDATE, el valor predeterminado de las filas afectadas es el número de filas realmente modificadas.
Si se especifica el indicador CLIENT_FOUND_ROWS en mysql_real_connect() al conectarse a mysqld, el valor de las 
filas afectadas es el número de filas "encontradas"; es decir, las que coinciden con la cláusula WHERE.

Si no se especifica este flag CLIENT_FOUND_ROWS pasa esto:

En MySQL, no es necesario comprobar el valor. MySQL no actualiza el registro si no hay cambios.
Esto significa que MySQL no incurre en la sobrecarga de registrar o escribir los datos.
Comprobar si algún valor ha cambiado tiene un pequeño coste, y creo que sí ejecuta los disparadores.

Para las sentencias UPDATE, el valor predeterminado de las filas afectadas es el número de filas realmente modificadas.

Un entero mayor que cero indica el número de filas afectadas o recuperadas.
Cero indica que no se actualizaron registros para una sentencia UPDATE, que ninguna fila coincidió con la cláusula WHERE
en la consulta o que aún no se ha ejecutado ninguna consulta.
"""

class DB:

    @staticmethod
    def db_connection():
        try:
            flags = [ClientFlag.FOUND_ROWS] #, -ClientFlag.LONG_FLAG]   #ver NOTA            
            cnx = mysql.connector.connect(
                host    = os.getenv("DB_HOST"),
                database= os.getenv("DB_NAME"),
                user    = os.getenv("DB_USER"),
                password= os.getenv("DB_PASSWORD"),
                port    = os.getenv("DB_PORT"),
                raise_on_warnings=True,
                charset ='utf8mb4',
                client_flags=flags
            )
            return cnx
        except Error as err:
            print(f'Error conexion: {err}')
        finally:
            print('Conexion finalizada')

    def read(sql: str, params: tuple = None) -> list[dict] | None:
        cnx = DB.db_connection()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(sql, params)
                print(sql)
                result = cursor.fetchall()
                print(result)
                return result if result else None
            except Error as err:
                print(f'Error lectura: {err}')
            finally:
                cursor.close()
                cnx.close()

    @staticmethod
    def write(sql: str, params: tuple) -> int | bool:
        cnx = DB.db_connection()
        with cnx.cursor() as cursor:
            try:
                cursor.execute(sql, params)
                cnx.commit()
                if cursor.lastrowid:
                    return cursor.lastrowid
                return cursor.rowcount
                #count = cursor.rowcount
                #return True if count > 0 else False
            except Error as err:
                cnx.rollback()
                print(f'Error escritura: {err}')
            finally:
                cursor.close()
                cnx.close()