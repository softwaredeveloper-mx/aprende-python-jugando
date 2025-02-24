pociones_magicas = {
    "curación": "Restaura tu salud",
    "invisibilidad": "Te hace invisible",
    "fuerza": "Aumenta tu poder"
}

print("Inicial",pociones_magicas)
pociones_magicas["velocidad"] = "Te hace más rápido"  # Agregar
print("Elemento Agregado",pociones_magicas)

del(pociones_magicas["invisibilidad"])  # Eliminar
print("Elemento Eliminado",pociones_magicas)

eliminado = pociones_magicas.pop("fuerza") #Sacar el elemento del diccionario
print("Se eliminó el elemento",eliminado)
print("Elemento Sacado",pociones_magicas)
