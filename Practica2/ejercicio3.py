rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

#Creo una lista con todas las lineas
lines = rules.splitlines()

#ingreso la palabra por teclado
keyword = input("Ingrese una palabra clave: ")

#tomo la linea de cada elemento de lines tal que la keyword se encuentre en la linea
# la funcion lower() en ambos argumentos lo hace case insensitive
res = [line for line in lines if keyword.lower() in line.lower()]

for i in res:
    print(i)
    print("linea")