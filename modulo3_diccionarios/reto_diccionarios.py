# RETO MODULO 3 - DICCIONARIOS EN PYTHON

inventario = {
    "laptop":    {"precio": 2500000, "stock": 5,  "categoria": "electronica"},
    "mouse":     {"precio": 85000,   "stock": 20, "categoria": "electronica"},
    "escritorio":{"precio": 750000,  "stock": 3,  "categoria": "muebles"},
    "silla":     {"precio": 450000,  "stock": 8,  "categoria": "muebles"},
    "teclado":   {"precio": 120000,  "stock": 15, "categoria": "electronica"},
}

print("--- Inventario completo ---")
for producto, datos in inventario.items():
    print(f"  {producto}: ${datos['precio']:,} | stock: {datos['stock']} | categoria: {datos['categoria']}")

print("\n--- Buscar producto ---")
buscar = "mouse"
if buscar in inventario:
    print(f"{buscar} encontrado:", inventario[buscar])
else:
    print(f"{buscar} no existe en el inventario")

print("\n--- Agregar producto ---")
inventario["monitor"] = {"precio": 980000, "stock": 7, "categoria": "electronica"}
print("monitor agregado. Total productos:", len(inventario))

print("\n--- Actualizar stock ---")
inventario["mouse"]["stock"] -= 3
print("Nuevo stock de mouse:", inventario["mouse"]["stock"])

print("\n--- Eliminar producto ---")
eliminado = inventario.pop("escritorio")
print("Eliminado:", eliminado)
print("Total productos:", len(inventario))

print("\n--- Productos por categoria ---")
categorias = {}
for producto, datos in inventario.items():
    cat = datos["categoria"]
    if cat not in categorias:
        categorias[cat] = []
    categorias[cat].append(producto)

for cat, productos in categorias.items():
    print(f"  {cat}: {productos}")

print("\n--- Producto mas caro ---")
mas_caro = max(inventario, key=lambda p: inventario[p]["precio"])
print(f"Mas caro: {mas_caro} -> ${inventario[mas_caro]['precio']:,}")

print("\n--- Valor total del inventario ---")
total = sum(d["precio"] * d["stock"] for d in inventario.values())
print(f"Valor total: ${total:,}")