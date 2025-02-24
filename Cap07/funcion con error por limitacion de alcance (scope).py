def funcion_local():
    mensaje = "Hola desde dentro de la función"
    print(mensaje)

funcion_local()
print(mensaje)  # Esto causará un error porque 'mensaje' no existe fuera de la función.
