zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


# separa el string en una lista de lineas
lines = zen.splitlines()
vocals = "AEIOUaeiou"

# guardo la linea para cada linea en la lista de lineas tal que la longitud de la lista de palabras sea mayor a 1 
# Y la palabra en la posicion 1 en la lista de palabras tenga la primera letra en vocals.
result = [line for line in lines if len(line.split()) >= 2 and line.split()[1][0] in vocals]

for i in result:
    print(i)
