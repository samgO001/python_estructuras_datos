# MODULO 2 - TUPLAS EN PYTHON


print("=" * 55)
print("       MODULO 2: TUPLAS EN PYTHON")
print("=" * 55)


# 1. CREACION DE TUPLAS

print("\n--- 1. Creacion de tuplas ---")

tupla_vacia = ()
coordenadas = (4.7110, -74.0721)
colores_rgb = (255, 128, 0)
datos_persona = ("Ana", 22, "Colombia")
un_elemento = (42,)

print("Tupla vacia:", tupla_vacia)
print("Coordenadas:", coordenadas)
print("Color RGB:", colores_rgb)
print("Datos persona:", datos_persona)
print("Un elemento:", un_elemento)
print("Tipo:", type(un_elemento))


# 2. ACCESO POR INDICE Y SLICING

print("\n--- 2. Acceso e indices ---")

print("Nombre:", datos_persona[0])
print("Edad:", datos_persona[1])
print("Pais:", datos_persona[2])
print("Ultimo:", datos_persona[-1])
print("Slice [0:2]:", datos_persona[0:2])


# 3. INMUTABILIDAD

print("\n--- 3. Inmutabilidad ---")

punto = (10, 20)
print("Punto:", punto)
try:
    punto[0] = 99
except TypeError as e:
    print("Error:", e)

# 4. DESEMPAQUETADO

print("\n--- 4. Desempaquetado ---")

nombre, edad, pais = datos_persona
print("nombre:", nombre)
print("edad:", edad)
print("pais:", pais)

primero, *resto = (1, 2, 3, 4, 5)
print("\nprimero:", primero)
print("resto:", resto)

*inicio, ultimo = (1, 2, 3, 4, 5)
print("inicio:", inicio)
print("ultimo:", ultimo)


# 5. METODOS DISPONIBLES

print("\n--- 5. Metodos de tuplas ---")

numeros = (3, 1, 4, 1, 5, 9, 2, 6, 1)
print("Tupla:", numeros)
print("count(1):", numeros.count(1))
print("index(5):", numeros.index(5))
print("len():", len(numeros))
print("max():", max(numeros))
print("min():", min(numeros))
print("sum():", sum(numeros))
print("sorted():", sorted(numeros))


# 6. TUPLAS ANIDADAS

print("\n--- 6. Tuplas anidadas ---")

tabla = (
    ("Nombre", "Edad", "Ciudad"),
    ("Carlos", 25, "Bogota"),
    ("Maria", 30, "Medellin"),
    ("Luis", 22, "Cali"),
)

for fila in tabla:
    print(fila)

print("\nEncabezado:", tabla[0])
print("Primer registro:", tabla[1])
print("Ciudad de Maria:", tabla[2][2])


# 7. CONVERSION ENTRE LISTA Y TUPLA

print("\n--- 7. Conversion lista <-> tupla ---")

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = tuple(mi_lista)
print("Lista a tupla:", mi_tupla)

de_vuelta = list(mi_tupla)
print("Tupla a lista:", de_vuelta)

print("\nEjemplos del Modulo 2 completados.")