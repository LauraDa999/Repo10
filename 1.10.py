def calcular_producto_punto(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        raise ValueError("Los arreglos deben tener la misma longitud.")
    return sum(a * b for a, b in zip(arreglo1, arreglo2))


arreglo_enteros1 = [2, 3, 4, 5]
arreglo_enteros2 = [1, 0, -2, 3]
producto_punto = calcular_producto_punto(arreglo_enteros1, arreglo_enteros2)
print(f"El producto punto de los arreglos enteros es: {producto_punto}")
