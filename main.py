try:
    b = float(input("Ingresa la base: "))
    h = float(input("Ingresa la altura: "))
    area = (b * h)
    print(f"El área del rectángulo es: {area}")
except ValueError:
    print("Por favor, ingresa solo números válidos.")
