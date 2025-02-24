agenda_magica = {
    "lunes": "Preparar pociones",
    "martes": "Entrenar hechizos",
    "miércoles": "Visitar el bosque encantado"
}

def mostrar_agenda():
    print("Agenda mágica:")
    for dia, tarea in agenda_magica.items():
        print(f"{dia.capitalize()}: {tarea}")

def agregar_tarea(dia, tarea):
    agenda_magica[dia] = tarea
    print(f"Tarea para {dia} agregada: {tarea}")

mostrar_agenda()
agregar_tarea("jueves", "Estudiar runas antiguas")
mostrar_agenda()
