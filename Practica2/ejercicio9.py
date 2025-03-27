clients = [
" Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
" Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
"luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
" ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
"carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
"alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
"patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
"MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
"SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
"Damián Castillo ", None, "", " "
]

#Creo una nueva lista de clientes sin espacios en blanco y sin None, capitalizo todos los nombres.
newclients = [client.strip().title() for client in clients if client is not None and client.strip()]
newclients2 = []

#Elimino los repetidos.
for client in newclients:
    if client not in newclients2:
        newclients2.append(client)

#imprimo resultado
for c in newclients2:
    print(c)

print()

#Usando un "set"
clientes = {client.strip().title() for client in clients if client is not None and client.strip()}
for i in sorted(clientes):
    print(i)