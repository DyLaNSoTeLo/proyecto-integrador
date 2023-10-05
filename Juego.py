import os,random, readchar
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
            
if __name__=="__main__":
    borrar_terminal() 

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


@dataclass
class Juego:
    laberinto: str
    pos_inicial: int
    pos_final: int

    def mover(self, new_px, new_py):
        
        def print_mapa(mapa):
            limpiar_pantalla()
            for row in mapa:
                print(''.join(row))

        def main_loop(mapa, start, end):
            px, py = start

            while (px, py) != end:
            mapa[py][px] = "P"
            print_mapa(mapa)
            mapa[py][px] = '.'
        
        key = readchar.readkey()
        
        if key == readchar.key.UP:
            new_py = py - 1
            if new_py >= 0 and mapa[new_py][px] != '#':
                py = new_py
        elif key == readchar.key.DOWN:
            new_py = py + 1
            if new_py < len(mapa) and mapa[new_py][px] != '#':
                py = new_py

        elif key == readchar.key.LEFT:
            new_px = px - 1
            if new_px >= 0 and mapa[py][new_px] != '#':
                px = new_px
                
        elif key == readchar.key.RIGHT:
            new_px = px + 1
            if new_px < len(mapa[py]) and mapa[py][new_px] != '#':
                px = new_px
                
    mapa[py][px] = "P"

    print_mapa(mapa)       
    print("Fin del juego!!")
    

        def main():

            start = (0, 0)
            end = (20, 20)
            maze = convert_labe_to_matrix(end)
            main_loop(maze, start, end)

        

        if __name__ == "__main__":

            main()
            
        print(f'Lo lograste!! {self.nombre},\n Felicidades eres el Ganador')