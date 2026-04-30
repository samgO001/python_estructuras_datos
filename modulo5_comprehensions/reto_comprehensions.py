# MODULO 5: RETO - COMPREHENSIONS

estudiantes = [
    {"nombre": "Ana Gomez",      "notas": [4.5, 3.8, 4.2, 3.5]},
    {"nombre": "Carlos Ruiz",    "notas": [2.5, 2.8, 3.0, 2.9]},
    {"nombre": "Diana Torres",   "notas": [5.0, 4.8, 4.9, 5.0]},
    {"nombre": "Eduardo Mora",   "notas": [1.5, 2.0, 2.5, 2.3]},
    {"nombre": "Fernanda Leon",  "notas": [3.5, 3.0, 3.2, 4.0]},
    {"nombre": "Gabriel Vargas", "notas": [3.8, 4.1, 3.9, 4.5]},
    {"nombre": "Hugo Salinas",   "notas": [2.9, 3.0, 2.8, 3.1]},
    {"nombre": "Isabel Castro",  "notas": [4.0, 3.5, 3.8, 4.2]},
]

asignaturas_por_estudiante = [
    {"nombre": "Ana Gomez",      "materias": ["Matematicas", "Programacion", "Fisica"]},
    {"nombre": "Carlos Ruiz",    "materias": ["Programacion", "Quimica"]},
    {"nombre": "Diana Torres",   "materias": ["Matematicas", "Fisica", "Quimica"]},
    {"nombre": "Eduardo Mora",   "materias": ["Matematicas", "Programacion"]},
    {"nombre": "Fernanda Leon",  "materias": ["Fisica", "Quimica", "Programacion"]},
]

NOTA_MINIMA = 3.0

def separador(titulo):
    print("\n" + "=" * 55)
    print(f"  {titulo}")
    print("=" * 55)


# 1. Calcular promedio de cada estudiante (dict comprehension)

separador("PROMEDIOS POR ESTUDIANTE")

promedios = {
    e["nombre"]: round(sum(e["notas"]) / len(e["notas"]), 2)
    for e in estudiantes
}

for nombre, promedio in promedios.items():
    print(f"  {nombre:<20} -> Promedio: {promedio}")


# 2. Clasificar aprobados y reprobados (list comprehension)

separador("CLASIFICACION")

aprobados = [nombre for nombre, prom in promedios.items() if prom >= NOTA_MINIMA]
reprobados = [nombre for nombre, prom in promedios.items() if prom < NOTA_MINIMA]

print("Aprobados:")
for a in aprobados:
    print(f"  - {a} ({promedios[a]})")

print("\nReprobados:")
for r in reprobados:
    print(f"  - {r} ({promedios[r]})")


# 3. Reporte completo (dict comprehension con logica)

separador("REPORTE COMPLETO")

reporte = {
    e["nombre"]: {
        "promedio": round(sum(e["notas"]) / len(e["notas"]), 2),
        "estado": "Aprobado" if sum(e["notas"]) / len(e["notas"]) >= NOTA_MINIMA else "Reprobado",
        "nota_maxima": max(e["notas"]),
        "nota_minima": min(e["notas"]),
    }
    for e in estudiantes
}

for nombre, datos in reporte.items():
    print(f"\n  {nombre}")
    print(f"    Promedio  : {datos['promedio']}")
    print(f"    Estado    : {datos['estado']}")
    print(f"    Nota max  : {datos['nota_maxima']}")
    print(f"    Nota min  : {datos['nota_minima']}")


# 4. Materias unicas en todo el curso (set comprehension)

separador("MATERIAS UNICAS EN EL CURSO")

materias_unicas = {
    materia
    for e in asignaturas_por_estudiante
    for materia in e["materias"]
}

print("Asignaturas registradas:")
for m in sorted(materias_unicas):
    print(f"  - {m}")


# 5. Estadisticas con generator expressions

separador("ESTADISTICAS GENERALES")

todos_los_promedios = list(promedios.values())

promedio_general = round(sum(p for p in todos_los_promedios) / len(todos_los_promedios), 2)
mejor_promedio   = max(p for p in todos_los_promedios)
peor_promedio    = min(p for p in todos_los_promedios)
total_aprobados  = sum(1 for p in todos_los_promedios if p >= NOTA_MINIMA)
total_reprobados = sum(1 for p in todos_los_promedios if p < NOTA_MINIMA)

mejor_nombre = [n for n, p in promedios.items() if p == mejor_promedio][0]
peor_nombre  = [n for n, p in promedios.items() if p == peor_promedio][0]

print(f"  Total estudiantes    : {len(estudiantes)}")
print(f"  Promedio general     : {promedio_general}")
print(f"  Mejor promedio       : {mejor_promedio} ({mejor_nombre})")
print(f"  Peor promedio        : {peor_promedio} ({peor_nombre})")
print(f"  Total aprobados      : {total_aprobados}")
print(f"  Total reprobados     : {total_reprobados}")
print(f"  Porcentaje aprobacion: {round(total_aprobados / len(estudiantes) * 100, 1)}%")


# 6. Notas por encima del promedio general (list comprehension)

separador("ESTUDIANTES SOBRE EL PROMEDIO GENERAL")

sobre_promedio = [
    (nombre, prom)
    for nombre, prom in promedios.items()
    if prom >= promedio_general
]

for nombre, prom in sorted(sobre_promedio, key=lambda x: x[1], reverse=True):
    print(f"  {nombre:<20} -> {prom}")