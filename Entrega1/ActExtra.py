'''El programa debe tener un menú interactivo que permita al usuario seleccionar las siguientes operaciones:
- Agregar un nuevo producto al inventario, solicitando al usuario el nombre y la cantidad inicial del producto.
- Eliminar un producto existente del inventario, solicitando al usuario el nombre del producto a eliminar.
- Mostrar el inventario actual, que incluya el nombre y la cantidad de cada producto.
- Salir del programa.

El inventario puede ser almacenado utilizando un diccionario simple, donde las claves sean los nombres de los productos y los valores sean las cantidades.
Se deben manejar situaciones simples como la introducción de productos duplicados o la eliminación de productos inexistentes.'''

def show_menu():  #Se muestra el menú en consola
    print("")
    print("---- Menú ----")
    print("1. Agregar producto al inventario")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    print("------------")


def add_prod(inv):  #Agrega un producto a la lista inv
    product = [input("Nombre: ").strip(), (input("cantidad: ").strip())]
    if not product[0].strip():
        print("Ingrese un nombre para el producto")
        return
    if product[1].isdigit():
        product[1] = int(product[1])
    else:
        print("Cantidad inválida.") # si la cantidad no es un numero, cancela la operacion
        return
    for item in inv:
        if item[0] == product[0] and product[0] != "":
            print(f"---El producto {product[0]} ya está en el inventario---") #Verifico que el producto no este en el inventario
            return
    if product[1] > 0: #Si la cantidad es un numero natural, agrega el prodcuto
        inv.append(product)
        print()
        print("---Producto agregado---")
    else:
        print()
        print("Cantidad errónea, ingrese el producto nuevamente") #Sino, cancela la operacion


def del_product(inv):
    print()
    if not inv:
        print("Inventario vacío.") #Verifico que la lista no este vacia
        return inv
    nom = input("Ingrese el nombre del producto a eliminar: ")
    new_inv = [i for i in inv if i[0] != nom] #Con comprension de listas, descarto los elementos en los que el nombre coincida
    if len(new_inv) == len(inv):
        print(f"No se encontró el producto {nom} en el inventario.") #Si las listas tienen el mismo tamaño, no eliminé nada
    else:
        print(f"Producto {nom} eliminado") #Sino, se eliminó un elemento
    return new_inv   #Devuelve la lista nueva


def show_inv(inv):
    print()
    if not inv:
        print("##Inventario vacío##") #Verifico lista inv vacia
        return
    print("--- Inventario ---")
    for producto in inv:   #imprimo todos los elementos de la lista
        for elem in producto:
            print(elem)
        print()
    print("------------")



def main():
    inv = []    #inicializo el inventario
    while True:   #Muestra el menu en bucle
        show_menu()
        option= (input("Ingrese el numero de opción: "))
        print("------------")
        if option == "1":
            add_prod(inv)
        elif option == "2":
            inv = del_product(inv)
        elif option == "3":
            show_inv(inv)
        elif option == "4":
            print("Cerrando el programa...")
            break
        else:
            print("Numero de opcion invalido")
            continue


main()  #Ejecuto el modulo main

