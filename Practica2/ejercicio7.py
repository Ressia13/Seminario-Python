import random;
import string;

def leerusuario():

    while True:
        user = input("Ingrese nombre de usuario: ").strip()
        date = input("Ingrese la fecha de hoy (AAAA/MM/DD)").strip()
        if len(user) <= 15:
            break
        else:
            print("El usuario no puede exceder los 15 caracteres.")
    return user, date


#Esto genera cadenas aleatorias (?)
def createcode(user, date):
    caracteres = string.ascii_letters + string.digits

    code = (f"{user.upper()}-{date.strip("/")}-")
    while len(code) < 30:
        code += random.choice(caracteres).upper()
    return code


user, date = leerusuario()
code = createcode(user, date)
print(f"Codigo de descuento: {code}")