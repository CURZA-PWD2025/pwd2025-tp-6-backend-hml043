import os
import mysql.connector

from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

class DB:

    @staticmethod
    def db_connection():
        try:
            cnx = mysql.connector.connect(
                host    = os.getenv("DB_HOST"),
                database= os.getenv("DB_NAME"),
                user    = os.getenv("DB_USER"),
                password= os.getenv("DB_PASSWORD"),
                port    = os.getenv("DB_PORT"),
                raise_on_warnings=True,
                charset ='utf8mb4'
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
                result = cursor.fetchall()
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
                count = cursor.rowcount
                return True if count > 0 else False
            except Error as err:
                cnx.rollback()
                print('Error escritura: {err}')
            finally:
                cursor.close()
                cnx.close()