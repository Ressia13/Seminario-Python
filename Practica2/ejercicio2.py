titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

#Con funcion max
print("funcion max: ", max(titles, key=len))

#manual
max = 0
for title in titles:
    if len(title) > max:
        max = len(title)
        titlemax = title
print("maximo manual: ", titlemax)
