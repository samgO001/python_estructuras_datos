# RETO MODULO 2 - TUPLAS EN PYTHON


ciudades = (
    ("Bogota",       4.7110,  -74.0721),
    ("Medellin",     6.2442,  -75.5812),
    ("Cali",         3.4516,  -76.5320),
    ("Barranquilla", 10.9685, -74.7813),
    ("Cartagena",    10.3910, -75.4794),
)

print("Ciudades registradas:", len(ciudades))

for ciudad in ciudades:
    nombre, lat, lon = ciudad
    print(f"  {nombre} -> lat: {lat}, lon: {lon}")

print("\nPrimera ciudad:", ciudades[0][0])
print("Ultima ciudad:", ciudades[-1][0])

latitudes = tuple(c[1] for c in ciudades)
print("\nLatitudes:", latitudes)
print("Latitud maxima:", max(latitudes))
print("Latitud minima:", min(latitudes))

ciudad_norte = max(ciudades, key=lambda c: c[1])
print("\nCiudad mas al norte:", ciudad_norte[0])

ciudad_sur = min(ciudades, key=lambda c: c[1])
print("Ciudad mas al sur:", ciudad_sur[0])

nueva = ("Bucaramanga", 7.1193, -73.1227)
ciudades_ampliadas = ciudades + (nueva,)
print("\nCiudades despues de agregar", nueva[0] + ":", len(ciudades_ampliadas))