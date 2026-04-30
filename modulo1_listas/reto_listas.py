# RETO MÓDULO 1 - LISTAS EN PYTHON


print("=" * 55)
print("   RETO MÓDULO 1: GESTOR DE NOTAS DE ESTUDIANTES")
print("=" * 55)

estudiante = "Carlos Andrés López"
notas = [3.5, 4.2, 2.8, 3.9, 4.5, 3.1, 2.5, 4.0]

print(f"\n Estudiante: {estudiante}")
print(f" Notas registradas: {notas}")

promedio = sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)

print(f"\n Estadísticas:")
print(f"   Total de notas : {len(notas)}")
print(f"   Promedio       : {promedio:.2f}")
print(f"   Nota máxima    : {nota_max}")
print(f"   Nota mínima    : {nota_min}")

estado = "APROBADO " if promedio >= 3.0 else "REPROBADO "
print(f"\n Estado académico: {estado}")

notas_ordenadas = sorted(notas, reverse=True)
print(f"\n Notas de mayor a menor: {notas_ordenadas}")

nueva_nota = 3.8
notas.append(nueva_nota)
print(f"\n Se agrega nota {nueva_nota}: {notas}")

nota_eliminada = min(notas)
notas.remove(nota_eliminada)
print(f"  Se elimina la nota más baja ({nota_eliminada}): {notas}")

nuevo_promedio = sum(notas) / len(notas)
nuevo_estado = "APROBADO " if nuevo_promedio >= 3.0 else "REPROBADO "

print(f"\n Después de los cambios:")
print(f"   Nuevo promedio : {nuevo_promedio:.2f}")
print(f"   Nuevo estado   : {nuevo_estado}")

sobre_promedio = [n for n in notas if n >= nuevo_promedio]
print(f"\n Notas por encima del promedio ({nuevo_promedio:.2f}): {sobre_promedio}")
print(f"   Cantidad: {len(sobre_promedio)} de {len(notas)}")

print("\n Reto Módulo 1 completado.")