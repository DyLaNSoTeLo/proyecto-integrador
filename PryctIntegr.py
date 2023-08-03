import readchar
from readchar import key

nombre= input("Introduzca su nombre: ")
print("!Bienvenido a esta nueva aventura, {}!".format(nombre))

 
while True:
    tecla = readchar.readkey()
    if tecla == key.UP:
        break
    print(tecla) 
