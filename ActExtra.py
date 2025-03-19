'''El programa debe tener un menú interactivo que permita al usuario seleccionar las siguientes operaciones:
- Agregar un nuevo producto al inventario, solicitando al usuario el nombre y la cantidad inicial del producto.
- Eliminar un producto existente del inventario, solicitando al usuario el nombre del producto a eliminar.
- Mostrar el inventario actual, que incluya el nombre y la cantidad de cada producto.
- Salir del programa.

El inventario puede ser almacenado utilizando un diccionario simple, donde las claves sean los nombres de los productos y los valores sean las cantidades.
Se deben manejar situaciones simples como la introducción de productos duplicados o la eliminación de productos inexistentes.'''

def show_menu():
    print("")
    print("---- Menú ----")
    print("1. Agregar producto al inventario")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    print("------------------")

def add_prod(inv):
    product = [input("Nombre: "), int(input("cantidad: "))]
    for item in inv:
        if item[0] == product[0]:
            print(f"---El producto {product[0]} ya está en el inventario---")
            return
    inv.append(product)
    print("---Producto agregado---")

def del_product():
    print()

def show_inv():
    print()



def main():
    inv = []
    while True:
        show_menu()
        option= (input("Ingrese el numero de opcion: "))
        if option == "1":
            add_prod(inv)
        elif option == "2":
            del_product()
        elif option == "3":
            show_inv()
        elif option == "4":
            print("Cerrando el programa...")
            break
        else:
            print("Numero de opcion invalido")
            break

main()

