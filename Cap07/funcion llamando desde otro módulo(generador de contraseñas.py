import random
import string

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation    
    pwd=""
    for _ in range(longitud):
        pwd = pwd + random.choice(caracteres)    
    return pwd

longitud = int(input("¿De que longitud quieres tu contraseña?: "))
pwdNueva = generar_password(longitud)
print(f"Esta es tu nueva contraseña: {pwdNueva}")



