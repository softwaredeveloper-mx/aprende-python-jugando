def area_rectangulo(base, altura):
    return base * altura

def volumen_caja(base, altura, profundidad):
    area = area_rectangulo(base, altura)  # Llamamos a otra función
    return area * profundidad


print(volumen_caja(2, 3, 4))  # Calcula el volumen de una caja
