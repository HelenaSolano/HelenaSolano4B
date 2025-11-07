from database import crear_conexion

def validar_credenciales(usuario, password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        consulta = "SELECT id_usuario FROM usuarios WHERE username = %s AND password = %s"
        cursor.execute(consulta, (usuario, password))
        result = cursor.fetchone()
        return bool(result)
    except Exception:
        return False
    finally:
        conexion.close()
