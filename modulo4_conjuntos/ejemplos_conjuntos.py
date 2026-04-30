# MODULO 4: CONJUNTOS (SETS)



# 1. Crear conjuntos

frutas = {"manzana", "naranja", "uva", "manzana"}
print("Conjunto de frutas:", frutas)


numeros = set([1, 2, 3, 4, 4, 5, 5])
print("Conjunto de numeros:", numeros)

conjunto_vacio = set()
print("Conjunto vacio:", conjunto_vacio)


# 2. Agregar y eliminar elementos

colores = {"rojo", "verde", "azul"}

colores.add("amarillo")
print("Despues de add:", colores)

colores.discard("verde")       
print("Despues de discard:", colores)

colores.remove("rojo")         
print("Despues de remove:", colores)

elemento = colores.pop()       
print("Elemento eliminado con pop:", elemento)
print("Conjunto tras pop:", colores)


# 3. Operaciones matematicas de conjuntos

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

union = a | b
print("Union:", union)
print("Union con metodo:", a.union(b))

interseccion = a & b
print("Interseccion:", interseccion)
print("Interseccion con metodo:", a.intersection(b))

diferencia = a - b
print("Diferencia a - b:", diferencia)
print("Diferencia con metodo:", a.difference(b))

dif_simetrica = a ^ b
print("Diferencia simetrica:", dif_simetrica)
print("Diferencia simetrica con metodo:", a.symmetric_difference(b))

# 4. Verificar relaciones entre conjuntos

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
z = {6, 7}

print("x es subconjunto de y:", x.issubset(y))       # True
print("y es superconjunto de x:", y.issuperset(x))   # True
print("x y z son disjuntos:", x.isdisjoint(z))       # True (sin elementos comunes)

# 5. Recorrer un conjunto

lenguajes = {"Python", "Java", "C++", "JavaScript"}
print("\nLenguajes de programacion:")
for lenguaje in lenguajes:
    print(" -", lenguaje)


# 6. Verificar pertenencia

print("\n'Python' en lenguajes:", "Python" in lenguajes)
print("'Ruby' en lenguajes:", "Ruby" in lenguajes)


# 7. Longitud y copia

print("\nTotal de lenguajes:", len(lenguajes))

copia = lenguajes.copy()
copia.add("Ruby")
print("Original:", lenguajes)
print("Copia modificada:", copia)


# 8. Frozenset: conjunto inmutable

dias_habiles = frozenset({"lunes", "martes", "miercoles", "jueves", "viernes"})
print("\nDias habiles (frozenset):", dias_habiles)



# 9. Convertir entre tipos

lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4]
sin_duplicados = list(set(lista_con_duplicados))
print("\nLista sin duplicados:", sin_duplicados)


# 10. Metodos adicionales: update, intersection_update

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print("\nDespues de update:", set1)

set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
set3.intersection_update(set4)
print("Despues de intersection_update:", set3)