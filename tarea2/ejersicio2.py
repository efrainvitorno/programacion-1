# Paso 1: Pedir al usuario cuántas frases ingresará
NumFraces = int(input("Ingrese el número de frases que ingresará: "))

# Paso 2: Listado de palabras obscenas
palabras_obscenas = ["mierda", "pendejo", "puta", "culero", "joder", "coño", "chingar", "verga", "coger", "marica", "cabrón", "pinche", "pendeja", "perra", "pelotudo", "cachudo", "culear", "reventar", "pito", "teta", "culiar", "chucha", "huevón", "chuchaqui", "cachar", "hueva", "carajo", "chimba", "pichar", "pirobo", "zorra", "cachete", "carepicha", "chingada", "joputa", "putamadre", "culiado", "gonorrea", "jueputa", "vulva", "pipí", "joto", "malparido"]

# Paso 3: Identificar las frases con palabras obscenas
FraceconObsena = []
FracessinContenidoObseno = []

for i in range(NumFraces):
    frase = input(f"Ingrese la frase {i+1}: ")
    tiene_PalabraObsena = False
    for PalabraObsena in palabras_obscenas:
        if PalabraObsena in frase:
            tiene_PalabraObsena = True
            frase = frase.replace(PalabraObsena, "*" * len(PalabraObsena))
    if tiene_PalabraObsena:
        FraceconObsena.append(frase)
    else:
        FracessinContenidoObseno.append(frase)

# Paso 4: Mostrar las frases con palabras obscenas tapadas con asteriscos
print("\nFrases con palabras obscenas tapadas con asteriscos:")
for i, frase in enumerate(FraceconObsena):
    print(f"Frase {i+1}: {frase}")

# Paso 5: Mostrar las frases que no tienen palabras obscenas
print("\nFrases sin palabras obscenas:")
for i, frase in enumerate(FracessinContenidoObseno):
    print(f"Frase {i+1}: {frase}")

# Paso 6: Ingreso de palabras para concatenar
PalabrasConcatenadas = input("\nIngrese palabras para concatenar las palabras obscenas (separadas por espacios): ").split()

# Paso 7: Concatenar las frases con palabras obscenas, reemplazando los asteriscos con las palabras ingresadas
ResultadoConcatenado = ''
for frase in FraceconObsena:
    if len(PalabrasConcatenadas) > 0:
        for palabra in PalabrasConcatenadas:
            frase = frase.replace('*', palabra, 1)
        ResultadoConcatenado += frase + ' '

# Paso 8: Mostrar el resultado final
print("\nResultado final:")
print(ResultadoConcatenado.strip())
