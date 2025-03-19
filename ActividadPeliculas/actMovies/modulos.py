

def durac_prom(lista):
    average = 0 if len(lista) == 0 else sum(lista) / len(lista)
    return average


# Código para probar las funciones solo si se ejecuta directamente este módulo
if __name__ == "__main__":
    print("Prueba de funciones en modulos.py")
    print(durac_prom([1, 2, 3, 4]))