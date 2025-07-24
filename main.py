import random
caracteres= "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
a = input("Escribe tu nombre de usuario:")
num_gen_pass = int(input("Hola" + a + "¿Cuántas contraseñas deseas generar?:"))
num_caracteres= int(input("de cuantos caracteres deseas tus contraseñas:"))

paswords={}
apps=[]
number=1

for i in range (num_gen_pass):
    name_app=input("Ingrese el nombre de la" + str(number) + "app:")
    apps.append(name_app)
    number += 1
for i in range(num_gen_pass):
    pas_gen = "".join(random.choices(caracteres, k=num_caracteres))
    paswords[apps[i]] = pas_gen 

print("\n¡Tus contraseñas han sido generadas con éxito!")
print("\nTus contraseñas generadas son:")
for app, contraseña in paswords.items():
    print(f"{app}: {contraseña}")
