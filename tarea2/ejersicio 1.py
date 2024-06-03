from functools import reduce

# Función para leer una lista de números enteros desde el teclado
def leer_lista(descripcion):
    while True:
        try:
            lista = list(map(int, input(f"Introduce los números de la {descripcion} separados por espacios: ").split()))
            return lista
        except ValueError:
            print("Error: Introduce solo números enteros.")

# Leer las dos listas desde el teclado
list1 = leer_lista("lista 1")
list2 = leer_lista("lista 2")
#X=elementos de linsta 1
#Y=elementos de las lista 2
# Verificar que las listas tienen el mismo tamaño ( de elementos)
if len(list1) != len(list2):
    print("Error: Las listas deben tener el mismo tamaño.")
else:
    # Paso 1: Crear todas las combinaciones posibles de pares (x, y) donde x es un elemento de list1 e y es el elemento correspondiente en list2
    TodosPares = [(x + y, x, y) for x in list1 for y in list2]

    # Paso 2: Filtrar pares donde x es mayor o igual que y
    ValordeSumas = [(ValorSumado, x, y) for ValorSumado, x, y in TodosPares if x >= y]

    # Paso 3: Encontrar el máximo valor de la lista de sumas
    # sorted  (ordenar la listas segun condicion de cada uno)
    if ValordeSumas:
        sorted_ValordeSumas = sorted(ValordeSumas, reverse=True)
        SumaMaxima, maximoX, maximoY = sorted_ValordeSumas[0]
        
        # Encontrar la suma competidora más cercana
        SumaPenultima = None
        for ValorSumado, x, y in sorted_ValordeSumas[1:]:
            if ValorSumado < SumaMaxima:
                SumaPenultima = ValorSumado
                break
                
        print("La suma mayor de los pares donde el primer número es mayor o igual que el segundo es:", SumaMaxima)
        print("La combinación que dio lugar a la suma mayor es:", maximoX, "+", maximoY)
        
        if SumaPenultima is not None:
            print("La suma competidora más cercana es:", SumaPenultima)
            for ValorSumado, x, y in sorted_ValordeSumas[1:]:
                if ValorSumado == SumaPenultima:
                    print("La combinación que dio lugar a la suma competidora más cercana es:", x, "+", y)
                    break
        else:
            print("No hay suma competidora más cercana.")
    else:
        print("No hay pares donde el primer número sea mayor o igual que el segundo.")
