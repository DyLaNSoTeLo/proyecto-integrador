import os, random, readchar
from dataclasses import dataclass
from typing import List
from functools import reduce


def leer_mapa(ruta: str):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()[1:]  # Leemos todas las líneas y omitimos la primera
        mapa = reduce(lambda x, y: x + y, lineas)  # Usamos reduce para concatenar todas las líneas en una sola cadena
        mapa = list(map(list, mapa.split('\n')))  # Convertimos la cadena en una lista de listas
    return mapa
@dataclass
class Juego:
    nombre: str
    mapa: List[List] = None
    pos_inicial: tuple = None
    pos_final: tuple = None
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_mapa(self):
        self.limpiar_pantalla()
        for row in self.mapa:
            print(' '.join(row))
            
    def main_loop(self):
        px, py = self.pos_inicial
        while (px, py) != self.pos_final:
            self.mapa[py][px] = "P"
            self.print_mapa()
            self.mapa[py][px] = '.'
            px, py = self.mover(px, py)
        print("Fin del juego!!")
        print(f'Lo lograste!! {self.nombre},\nFelicidades eres el Ganador')
            
    def mover(self, px, py):
        new_px, new_py = px, py
        
        tecla = readchar.readkey()
        if tecla == readchar.key.UP:
            new_py = py - 1
            if new_py >= 0 and self.mapa[new_py][px] != '#':
                py = new_py
            
        elif tecla == readchar.key.DOWN:
            new_py = py + 1
            if new_py < len(self.mapa) and self.mapa[new_py][px] != '#':
                py = new_py
                
        elif tecla == readchar.key.LEFT:
            new_px = px - 1
            if new_px >= 0 and self.mapa[py][new_px] != '#':
                px = new_px
                
        elif tecla == readchar.key.RIGHT:
            new_px = px + 1
            if new_px < len(self.mapa[py]) and self.mapa[py][new_px] != '#':
                px = new_px
                
        return px, py

def main():
    nombre= input("Introduzca su nombre: ")
    print("!Bienvenido a esta nueva aventura, {}!".format(nombre))
    
    lista_mapas = os.listdir("proyecto-integrador/mapas/")
    ruta_mapa = random.choice(lista_mapas)
    
    mapa = leer_mapa("proyecto-integrador/mapas/"+ruta_mapa)
    pos_inicial = (0, 0)  
    pos_final = (19, 20)
    
    juego = Juego(nombre, mapa, pos_inicial, pos_final)
    
    juego.main_loop()

if __name__ == "__main__":
    main()
