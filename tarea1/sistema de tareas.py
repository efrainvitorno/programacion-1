# Función para agregar una tarea
def AgregarTarea(tareas, titulo, descripcion):
    tareas.append((titulo, descripcion, "pendiente"))

# Función para marcar una tarea como "en curso"
def TareaEnCurso(tareas, titulo):
    for i, (t, d, estado) in enumerate(tareas):
        if t == titulo:
            tareas[i] = (t, d, "en curso")
            break  # salir del bucle

# Función para marcar una tarea como "completada"
def TareaCompletada(tareas, titulo):
    for i, (t, d, estado) in enumerate(tareas):
        if t == titulo:
            tareas[i] = (t, d, "completada")
            break # salir del bucle

# Función para eliminar una tarea
def EliminarTarea(tareas, titulo):
    for i, (t, d, estado) in enumerate(tareas):
        if t == titulo:
            del tareas[i]
            break # salir del bucle

# Función para editar el estado de una tarea
def EditarEstado(tareas, titulo, nuevo_estado):
    for i, (t, d, estado) in enumerate(tareas):
        if t == titulo:
            tareas[i] = (t, d, nuevo_estado)
            break # salir del bucle

# Función principal para gestionar tareas
def gestionar_tareas(tareas, gestionar, *args):
    gestionar(tareas, *args)

# Función para mostrar la lista de tareas
def mostrar_tareas(tareas):
    for titulo, descripcion, estado in tareas:
        print(f"Tarea: {titulo}, Descripción: {descripcion}, Estado: {estado}")

# Lista inicial de tareas vacía
tareas = []

# Bucle principal para la interacción con el usuario
while True:
    comando = input("Ingrese un comando (agregar, en curso, completada, eliminar, listar, editar, salir): ")
    if comando == "agregar":
        titulo = input("Título de la tarea: ")
        descripcion = input("Descripción de la tarea: ")
        gestionar_tareas(tareas, AgregarTarea, titulo, descripcion)
    elif comando == "en curso":
        titulo = input("Título de la tarea: ")
        gestionar_tareas(tareas, TareaEnCurso, titulo)
    elif comando == "completada":
        titulo = input("Título de la tarea: ")
        gestionar_tareas(tareas, TareaCompletada, titulo)
    elif comando == "eliminar":
        titulo = input("Título de la tarea: ")
        gestionar_tareas(tareas, EliminarTarea, titulo)
    elif comando == "listar":
        mostrar_tareas(tareas)
    elif comando == "editar":
        titulo = input("Título de la tarea: ")
        nuevo_estado = input("Nuevo estado de la tarea (pendiente, en curso, completada): ")
        if nuevo_estado in ["pendiente", "en curso", "completada"]:
            gestionar_tareas(tareas, EditarEstado, titulo, nuevo_estado)
        else:
            print("Estado no válido. Use 'pendiente', 'en curso', o 'completada'.")
    elif comando == "salir":
        break
    else:
        print("Comando no reconocido.")
