from database import crear_conexion

#VER PRODUCTOS 
def ver_productos():
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre_producto, marca, precio, stock FROM productos")
        productos = cursor.fetchall()
        return productos
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        return []
    finally:
        conexion.close()


#AGREGAR PRODUCTO 
def agregar_producto(nombre_producto, marca, precio, stock):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre_producto, marca, precio, stock) VALUES (%s, %s, %s, %s)", (nombre_producto, marca, precio, stock))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al agregar producto: {e}")
        return False
    finally:
        conexion.close()


#ACTUALIZAR PRODUCTO
def actualizar_producto(id_producto, nombre_producto, marca, precio, stock):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET nombre_producto=%s, marca=%s, precio=%s, stock=%s WHERE id_producto=%s", (nombre_producto, marca, precio, stock, id_producto))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        return False
    finally:
        conexion.close()


#ELIMINAR PRODUCTO 
def eliminar_producto(id_producto):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto=%s", (id_producto,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        return False
    finally:
        conexion.close()
