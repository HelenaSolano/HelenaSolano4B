from database import crear_conexion

def ver_usuarios():
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_usuario, username FROM usuarios")
        return cursor.fetchall()
    except Exception:
        return []
    finally:
        conexion.close()


def agregar_usuarios(username, password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, password))
        conexion.commit()
        return True
    except Exception:
        return False
    finally:
        conexion.close()


def actualizar_usuarios(id_usuario, new_usuario, new_password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET username = %s, password = %s WHERE id_usuario = %s"
        cursor.execute(sql, (new_usuario, new_password, id_usuario))
        conexion.commit()
        return True
    except Exception:
        return False
    finally:
        conexion.close()


def eliminar_usuarios(id_usuario):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        return False
    finally:
        conexion.close()
