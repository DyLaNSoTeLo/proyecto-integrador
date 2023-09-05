import os, readchar
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
    print("Borrar terminal")
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
               
def parse_laberinto(labe_string):

    return [list(row) for row in labe_string.split("\n")]   

def convert_labe_to_matrix(end):
  
    labe_string = """
..###################
....#.......#.......#
###.#.#.#####.#.#.#.#
#.#.#.#...#.#.#.#.#.#
#.#.#.#####.#.#####.#
#...#...#.....#...#.#
###.#.###.###.###.#.#
#.#.#.....#...#.....#
#.#.#.#.###.###.###.#
#.....#.#...#.....#.#
#.#.#.###.#####.#####
#.#.#.#...#...#.#...#
###.###.#.#.#.#.#.#.#
#.#.#.#.#...#.#...#.#
#.#.#.#####.#####.###
#.....#...#.#.#...#.#
#.#######.#.#.###.#.#
#.....#.#.....#.#...#
#######.###.#.#.###.#
#...........#.#.....#
###################..
"""
    labe_string = labe_string.replace("end", str(end[0]) + ", " + str(end[1]))

    labe_string = labe_string.strip()

    return parse_laberinto(labe_string)

 

def main():

    start = (0, 0)

    end = (20, 20)

    maze = convert_labe_to_matrix(end)

    main_loop(maze, start, end)

 

if __name__ == "__main__":

    main()