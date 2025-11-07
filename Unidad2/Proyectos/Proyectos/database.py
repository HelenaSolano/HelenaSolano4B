import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="poo_proyecto_parcial2"
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        return None
