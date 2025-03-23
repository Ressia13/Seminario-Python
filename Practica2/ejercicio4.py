username = input("Ingrese nombre de usuario (Debe contener mayuscula, minuscula, numero y sin caracteres esp): ")

valid = False
if len(username) >= 5:
    if any(char.isdigit() for char in username):
        if any(char.isupper() for char in username):
            if username.isalnum():
                print(f"Nombre de usuario {username} valido.")
                valid =True
if valid == False:
    print(f"Nombre de usuario {username} invalido.")

