# Repo10
# 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```
def calcular_promedio(arreglo):
    if not arreglo:
        return 0
    return sum(arreglo) / len(arreglo)


numeros_reales = [4.5, 3.2, 6.7, 8.1, 5.5]
promedio = calcular_promedio(numeros_reales)
print(f"El promedio de los números reales es: {promedio}")

```
# 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```
def calcular_producto_punto(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        raise ValueError("Los arreglos deben tener la misma longitud.")
    return sum(a * b for a, b in zip(arreglo1, arreglo2))


arreglo_enteros1 = [2, 3, 4, 5]
arreglo_enteros2 = [1, 0, -2, 3]
producto_punto = calcular_producto_punto(arreglo_enteros1, arreglo_enteros2)
print(f"El producto punto de los arreglos enteros es: {producto_punto}")

```
#  3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```
def dejar_ceros_al_final(arreglo):
    return [x for x in arreglo if x != 0] + [0] * arreglo.count(0)


arreglo_con_ceros = [2, 0, 5, 0, 8, 0, 1, 0, 3]
arreglo_resultante = dejar_ceros_al_final(arreglo_con_ceros)
print(f"Arreglo con ceros al final: {arreglo_resultante}")

```
