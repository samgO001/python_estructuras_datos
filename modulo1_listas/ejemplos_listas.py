# MÓDULO 1 - LISTAS EN PYTHON


print("=" * 55)
print("       MÓDULO 1: LISTAS EN PYTHON")
print("=" * 55)

# 1. CREACIÓN DE LISTAS

print("\n--- 1. Creación de listas ---")

lista_vacia = []
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza", "durazno"]
mixta = [10, "hola", 3.14, True, None]

print(f"Lista vacía:    {lista_vacia}")
print(f"Números:        {numeros}")
print(f"Frutas:         {frutas}")
print(f"Lista mixta:    {mixta}")


# 2. ACCESO POR ÍNDICE Y SLICING

print("\n--- 2. Acceso por índice y slicing ---")

print(f"Primera fruta:         {frutas[0]}")
print(f"Última fruta:          {frutas[-1]}")
print(f"Frutas [1:3]:          {frutas[1:3]}")
print(f"Frutas hasta índice 2: {frutas[:2]}")
print(f"Frutas desde índice 2: {frutas[2:]}")
print(f"Frutas al revés:       {frutas[::-1]}")

# 3. MÉTODOS PRINCIPALES

print("\n--- 3. Métodos de listas ---")

colores = ["rojo", "verde", "azul"]
print(f"Lista original: {colores}")

colores.append("amarillo")
print(f"append('amarillo'): {colores}")

colores.insert(1, "naranja")
print(f"insert(1, 'naranja'): {colores}")

colores.remove("verde")
print(f"remove('verde'): {colores}")

eliminado = colores.pop()
print(f"pop() eliminó '{eliminado}': {colores}")

eliminado_idx = colores.pop(0)
print(f"pop(0) eliminó '{eliminado_idx}': {colores}")

colores.sort()
print(f"sort(): {colores}")

colores.reverse()
print(f"reverse(): {colores}")

print(f"len(): {len(colores)}")
print(f"count('azul'): {colores.count('azul')}")
print(f"index('azul'): {colores.index('azul')}")


# 4. RECORRER UNA LISTA

print("\n--- 4. Recorrer una lista ---")

animales = ["perro", "gato", "loro", "conejo"]

print("Con for simple:")
for animal in animales:
    print(f"  - {animal}")

print("Con enumerate:")
for i, animal in enumerate(animales):
    print(f"  [{i}] {animal}")


# 5. OPERACIONES CON LISTAS

print("\n--- 5. Operaciones con listas ---")

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

concatenada = lista_a + lista_b
print(f"Concatenación: {lista_a} + {lista_b} = {concatenada}")

repetida = lista_a * 3
print(f"Repetición: {lista_a} * 3 = {repetida}")

print(f"3 en lista_a: {3 in lista_a}")
print(f"9 en lista_a: {9 in lista_a}")

# 6. LISTAS ANIDADAS (MATRICES)

print("\n--- 6. Listas anidadas ---")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 3x3:")
for fila in matriz:
    print(f"  {fila}")

print(f"Elemento [1][2]: {matriz[1][2]}")

print("\n Ejemplos del Módulo 1 completados.")