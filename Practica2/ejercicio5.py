react_time = int(input("Ingrese el tiepmo de reaccion en ms: "))

categorias = {
    "Rapido" : range(0, 200),
    "Normal" : range(200, 501),
    "Lento" : range(501, 1001)
}

for categoria, rango in categorias.items():
    if react_time in rango:
        print(f"El tiempo de reaccion es {categoria}")
        break
else:
    print("Valor fuera de rango.")