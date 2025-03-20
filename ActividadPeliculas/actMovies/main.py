"""Queremos saber:
¿Cuál fue la duración promedio, en minutos, de todas las películas?
¿Cuántas películas duran más que el promedio, en minutos?"""

import modulos

movies_duration = [108, 105, 112, 115, 123, 129, 122, 140]

print("la duracion promedio de las películas es: ", modulos.durac_prom(movies_duration))
more_than = [i for i in movies_duration if modulos.durac_prom(movies_duration) < i]
print(len(more_than))
