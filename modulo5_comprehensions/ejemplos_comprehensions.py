# MODULO 5: COMPREHENSIONS



# 1. LIST COMPREHENSION


cuadrados = [x ** 2 for x in range(1, 11)]
print("Cuadrados:", cuadrados)

pares = [x for x in range(1, 21) if x % 2 == 0]
print("Pares:", pares)

frutas = ["manzana", "naranja", "uva", "pera"]
mayusculas = [fruta.upper() for fruta in frutas]
print("Frutas en mayusculas:", mayusculas)

palabras = ["sol", "programacion", "luz", "estructuras", "py", "datos"]
largas = [p for p in palabras if len(p) > 4]
print("Palabras largas:", largas)

longitudes = [(p, len(p)) for p in palabras]
print("Longitudes:", longitudes)


# 2. LIST COMPREHENSION CON CONDICIONAL TERNARIO

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
etiquetas = ["par" if n % 2 == 0 else "impar" for n in numeros]
print("\nEtiquetas par/impar:", etiquetas)


temps = [15, 22, 35, 8, 28, 10]
clasificacion = ["calor" if t >= 25 else "frio" for t in temps]
print("Clasificacion de temperaturas:", clasificacion)


# 3. LIST COMPREHENSION ANIDADA

tabla = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
for linea in tabla:
    print(linea)


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [num for fila in matriz for num in fila]
print("\nMatriz aplanada:", plana)


# 4. DICT COMPREHENSION


cuadrados_dict = {x: x ** 2 for x in range(1, 6)}
print("\nCuadrados (dict):", cuadrados_dict)

longitudes_dict = {p: len(p) for p in palabras}
print("Longitudes (dict):", longitudes_dict)

original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print("Diccionario invertido:", invertido)

frutas_largas = {f: len(f) for f in frutas if len(f) > 4}
print("Frutas con nombre largo:", frutas_largas)

paises = ["Colombia", "Mexico", "Argentina"]
capitales = ["Bogota", "Ciudad de Mexico", "Buenos Aires"]
pais_capital = {p: c for p, c in zip(paises, capitales)}
print("Paises y capitales:", pais_capital)


# 5. SET COMPREHENSION


cuadrados_set = {x ** 2 for x in range(-5, 6)}
print("\nCuadrados unicos (set):", cuadrados_set)

nombres = ["Ana", "Alberto", "Carlos", "Camila", "David"]
iniciales = {n[0] for n in nombres}
print("Iniciales unicas:", iniciales)

long_unicas = {len(p) for p in palabras}
print("Longitudes unicas:", long_unicas)


# 6. GENERATOR EXPRESSION


generador = (x ** 2 for x in range(1, 6))
print("\nGenerador de cuadrados:")
for valor in generador:
    print(" ", valor)

total = sum(x ** 2 for x in range(1, 11))
print("Suma de cuadrados del 1 al 10:", total)

maximo = max(len(p) for p in palabras)
print("Longitud maxima de palabras:", maximo)


# 7. COMPREHENSION CON FUNCIONES

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = [n for n in range(2, 50) if es_primo(n)]
print("\nNumeros primos hasta 50:", primos)

def formatear(nombre):
    return nombre.strip().title()

nombres_sucios = ["  ana  ", "CARLOS", "diana torres", " maria "]
nombres_limpios = [formatear(n) for n in nombres_sucios]
print("Nombres formateados:", nombres_limpios)