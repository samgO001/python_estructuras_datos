# MODULO 4: RETO - CONJUNTOS


def mostrar_separador(titulo):
    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)


def mostrar_conjunto(nombre, conjunto):
    print(f"{nombre} ({len(conjunto)} estudiantes):")
    for estudiante in sorted(conjunto):
        print(f"   - {estudiante}")


def verificar_estudiante(nombre, *conjuntos, nombres_conjuntos):
    print(f"\nBuscando a '{nombre}':")
    encontrado = False
    for conjunto, nombre_conjunto in zip(conjuntos, nombres_conjuntos):
        if nombre in conjunto:
            print(f"   Inscrito en: {nombre_conjunto}")
            encontrado = True
    if not encontrado:
        print("   No encontrado en ninguna materia.")



matematicas = {
    "Ana Gomez",
    "Carlos Ruiz",
    "Diana Torres",
    "Eduardo Mora",
    "Fernanda Leon",
    "Gabriel Vargas",
}

programacion = {
    "Carlos Ruiz",
    "Diana Torres",
    "Hugo Salinas",
    "Isabel Castro",
    "Fernanda Leon",
    "Jorge Mendez",
}


# 1. Mostrar los grupos originales

mostrar_separador("GRUPOS ORIGINALES")
mostrar_conjunto("Matematicas", matematicas)
print()
mostrar_conjunto("Programacion", programacion)


# 2. Operaciones entre conjuntos

mostrar_separador("OPERACIONES DE CONJUNTOS")

en_ambas = matematicas & programacion
print("Estudiantes en AMBAS materias (interseccion):")
for e in sorted(en_ambas):
    print(f"   - {e}")

todos = matematicas | programacion
print(f"\nTotal de estudiantes distintos (union): {len(todos)}")
for e in sorted(todos):
    print(f"   - {e}")

solo_matematicas = matematicas - programacion
print("\nEstudiantes SOLO en Matematicas (diferencia):")
for e in sorted(solo_matematicas):
    print(f"   - {e}")

solo_programacion = programacion - matematicas
print("\nEstudiantes SOLO en Programacion (diferencia):")
for e in sorted(solo_programacion):
    print(f"   - {e}")

en_una_sola = matematicas ^ programacion
print("\nEstudiantes en UNA sola materia (diferencia simetrica):")
for e in sorted(en_una_sola):
    print(f"   - {e}")


# 3. Verificar estudiantes

mostrar_separador("VERIFICACION DE ESTUDIANTES")
verificar_estudiante(
    "Carlos Ruiz",
    matematicas, programacion,
    nombres_conjuntos=["Matematicas", "Programacion"]
)
verificar_estudiante(
    "Hugo Salinas",
    matematicas, programacion,
    nombres_conjuntos=["Matematicas", "Programacion"]
)
verificar_estudiante(
    "Maria Perez",
    matematicas, programacion,
    nombres_conjuntos=["Matematicas", "Programacion"]
)


# 4. Agregar y eliminar estudiantes

mostrar_separador("ACTUALIZACION DE GRUPOS")

nuevo = "Laura Pineda"
matematicas.add(nuevo)
print(f"'{nuevo}' agregada a Matematicas.")

retirado = "Ana Gomez"
matematicas.discard(retirado)
print(f"'{retirado}' retirada de Matematicas.")

print(f"\nMatematicas actualizada ({len(matematicas)} estudiantes):")
for e in sorted(matematicas):
    print(f"   - {e}")


# 5. Estadisticas finales

mostrar_separador("ESTADISTICAS FINALES")

todos_final = matematicas | programacion
en_ambas_final = matematicas & programacion
solo_mat_final = matematicas - programacion
solo_prog_final = programacion - matematicas

print(f"Total de estudiantes distintos : {len(todos_final)}")
print(f"Inscritos en ambas materias    : {len(en_ambas_final)}")
print(f"Solo en Matematicas            : {len(solo_mat_final)}")
print(f"Solo en Programacion           : {len(solo_prog_final)}")
print(f"Matematicas no tiene alumnos de programacion: {matematicas.isdisjoint(programacion)}")