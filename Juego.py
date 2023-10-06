import os, random, readchar
from dataclasses import dataclass
from readchar import key


nombre= input("Introduzca su nombre: ")
print("!Bienvenido a esta nueva aventura, {}!".format(nombre))

while True:
    tecla_1 = readchar.readkey()
    if tecla_1 == key.UP:
        break
    print(tecla_1)
    
def borrar_terminal():
    numveces =0
    while numveces < 50:
        tecla_1 = readchar.readkey()
        if ord(tecla_1)>0:
            os.system('cls' if os.name=='nt' else 'clear')
            numveces=numveces+1
            print(numveces)
            
def leer_mapa(proyecto-integrador\mapas):
    with open(proyecto-integrador\mapas, 'r') as archivo:
        mapa = [list(linea.strip()) for linea in proyecto-integrador\mapas]
    return mapa
            
@dataclass
class Juego:
    nombre: str
    mapa: list = None
    pos_inicial: tuple = None
    pos_final: tuple = None
    
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_mapa(self):
        self.limpiar_pantalla()
        for row in self.mapa:
            print(''.join(row))

    def main_loop(self):
        px, py = self.pos_inicial

        while (px, py) != self.pos_final:
            self.mapa[py][px] = "P"
            self.print_mapa()
            self.mapa[py][px] = '.'
            px, py = self.mover(px, py)
            print("Fin del juego!!")
            print(f'Lo lograste!! {self.nombre},\n Felicidades eres el Ganador')

    def mover(self, px, py):
        new_px, new_py = px, py
        
        key = readchar.readkey()
        
        if key == readchar.key.UP:
            new_py = py - 1
        if new_py >= 0 and self.mapa[new_py][px] != '#':
            py = new_py
            
        elif key == readchar.key.DOWN:
            new_py = py + 1
        if new_py < len(self.mapa) and self.mapa[new_py][px] != '#':
            py = new_py

        elif key == readchar.key.LEFT:
            new_px = px - 1
        if new_px >= 0 and self.mapa[py][new_px] != '#':
            px = new_px
                
        elif key == readchar.key.RIGHT:
            new_px = px + 1
        if new_px < len(self.mapa[py]) and self.mapa[py][new_px] != '#':
            px = new_px
                
        return px, py

          
def main():
    nombre= input("Introduzca su nombre: ")
    print("!Bienvenido a esta nueva aventura, {}!".format(nombre))
    
    mapa = leer_mapa('nombre_del_archivo.txt') 
    pos_inicial = (0, 0)  
    pos_final = (0, 0)
    
    juego = Juego(nombre, mapa, pos_inicial, pos_final)
    
    juego.main_loop()

if __name__ == "__main__":
    main()