# Datos de los alumnos
alumnos = []
CantidadAlumnos = 0

# Función para definir la cantidad de alumnos del salón
def DefinirCantidadAlumnos():
    global CantidadAlumnos
    CantidadAlumnos = int(input("Ingrese la cantidad de alumnos del salón: "))
    print(f"Cantidad de alumnos del salón definida en {CantidadAlumnos}.\n")

# Función para agregar un alumno
def AgregarAlumno():
    if len(alumnos) >= CantidadAlumnos:
        print("No se pueden agregar más alumnos, se ha alcanzado la cantidad máxima definida.\n")
        return
    codigo = input("Ingrese el código del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    promedio = float(input("Ingrese el promedio general del alumno: "))
    alumnos.append({'codigo': codigo, 'nombre': nombre, 'promedio': promedio})
    print("Alumno agregado exitosamente.\n")

# Función para eliminar un alumno
def EliminarAlumno():
    codigo = input("Ingrese el código del alumno a eliminar: ")
    for alumno in alumnos:
        if alumno['codigo'] == codigo:
            alumnos.remove(alumno)
            print("Alumno eliminado exitosamente.\n")
            return
    print("Alumno no encontrado.\n")

# Función para modificar un alumno
def ModificarAlumno():
    codigo = input("Ingrese el código del alumno a modificar: ")
    for alumno in alumnos:
        if alumno['codigo'] == codigo:
            nombre = input("Ingrese el nuevo nombre del alumno: ")
            promedio = float(input("Ingrese el nuevo promedio general del alumno: "))
            alumno['nombre'] = nombre
            alumno['promedio'] = promedio
            print("Alumno modificado exitosamente.\n")
            return
    print("Alumno no encontrado.\n")

# Función para mostrar todos los alumnos
def MostrarAlumnos():
    if not alumnos:
        print("No hay alumnos registrados.\n")
        return
    for alumno in alumnos:
        print(f"Código: {alumno['codigo']}, Nombre: {alumno['nombre']}, Promedio: {alumno['promedio']}")
    print()

# Función para calcular el promedio del salón
def PromedioSalon():
    if not alumnos:
        print("No hay alumnos registrados.\n")
        return
    suma_promedios = sum(alumno['promedio'] for alumno in alumnos)
    promedio = suma_promedios / len(alumnos)
    print(f"El promedio del salón es: {promedio:.2f}\n")

# Menú de interacción
def menu():
    while True:
        print("1. Definir cantidad de alumnos")
        print("2. Agregar alumno")
        print("3. Eliminar alumno")
        print("4. Modificar alumno")
        print("5. Mostrar alumnos")
        print("6. Promedio del salón")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            DefinirCantidadAlumnos()
        elif opcion == '2':
            AgregarAlumno()
        elif opcion == '3':
            EliminarAlumno()
        elif opcion == '4':
            ModificarAlumno()
        elif opcion == '5':
            MostrarAlumnos()
        elif opcion == '6':
            PromedioSalon()
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar el menú
menu()
