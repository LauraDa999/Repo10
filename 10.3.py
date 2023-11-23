def dejar_ceros_al_final(arreglo):
    
    return [x for x in arreglo if x != 0] + [0] * arreglo.count(0)


arreglo_con_ceros = [2, 0, 5, 0, 8, 0, 1, 0, 3]
arreglo_resultante = dejar_ceros_al_final(arreglo_con_ceros)
print(f"Arreglo con ceros al final: {arreglo_resultante}")
