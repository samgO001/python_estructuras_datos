# MODULO 3 - DICCIONARIOS EN PYTHON

print("=" * 55)
print("       MODULO 3: DICCIONARIOS EN PYTHON")
print("=" * 55)


# 1. CREACION DE DICCIONARIOS

print("\n--- 1. Creacion de diccionarios ---")

vacio = {}
persona = {"nombre": "Carlos", "edad": 25, "ciudad": "Bogota"}
producto = dict(nombre="laptop", precio=2500000, stock=10)

print("Vacio:", vacio)
print("Persona:", persona)
print("Producto:", producto)


# 2. ACCESO A VALORES

print("\n--- 2. Acceso a valores ---")

print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Con get():", persona.get("telefono", "No registrado"))


# 3. AGREGAR Y MODIFICAR

print("\n--- 3. Agregar y modificar ---")

persona["telefono"] = "3001234567"
print("Despues de agregar telefono:", persona)

persona["edad"] = 26
print("Despues de modificar edad:", persona)


# 4. ELIMINAR ELEMENTOS

print("\n--- 4. Eliminar elementos ---")

eliminado = persona.pop("telefono")
print("pop('telefono') elimino:", eliminado)
print("Diccionario:", persona)

persona["temporal"] = "borrar"
del persona["temporal"]
print("Despues de del:", persona)


# 5. METODOS PRINCIPALES

print("\n--- 5. Metodos ---")

print("keys():", list(persona.keys()))
print("values():", list(persona.values()))
print("items():", list(persona.items()))
print("len():", len(persona))
print("'edad' in persona:", "edad" in persona)


# 6. RECORRER UN DICCIONARIO

print("\n--- 6. Recorrer diccionario ---")

for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# 7. DICCIONARIOS ANIDADOS

print("\n--- 7. Diccionarios anidados ---")

estudiantes = {
    "est001": {"nombre": "Ana", "nota": 4.5, "ciudad": "Cali"},
    "est002": {"nombre": "Luis", "nota": 3.8, "ciudad": "Bogota"},
    "est003": {"nombre": "Maria", "nota": 4.0, "ciudad": "Medellin"},
}

for codigo, datos in estudiantes.items():
    print(f"  {codigo} -> {datos['nombre']} | Nota: {datos['nota']}")

print("Nota de Ana:", estudiantes["est001"]["nota"])


# 8. METODOS UTILES

print("\n--- 8. Otros metodos ---")

config = {"host": "localhost", "puerto": 8080, "debug": True}
copia = config.copy()
print("Copia:", copia)

config.update({"puerto": 9090, "version": "1.0"})
print("Despues de update():", config)

config.clear()
print("Despues de clear():", config)

print("\nEjemplos del Modulo 3 completados.")