import math
print("--- Calculadora de Áreas ---")
opcion = input("¿Qué quieres calcular? (1: Rectángulo, 2: Círculo): ")

if opcion == "1":
    b = float(input("Ingresa la base: "))
    h = float(input("Ingresa la altura: "))
    area_rectangulo = (b * h)
    print(f"El área es: {area_rectangulo}")
elif opcion == "2":
    r = float(input("Ingresa el radio: "))
    area_circulo = math.pi * (r ** 2)
    print(f"El área es: {area_circulo}")
else:
    print("Opción no válida")
