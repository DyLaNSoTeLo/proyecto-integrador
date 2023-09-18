import os, readchar, random 
from dataclasses import dataclass
from readchar import key


@dataclass
class Juego():
    nombre : str
    labe_string : str

        
    def matrix(self):
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     

    if (0 <= new_y <=  len(self.labe_string) 
        and 0 <= new_x <= len(self.labe_string[0])
        and self.labe_string[new_y][new_x] != "#"):
        self.labe_stringx[y][x] = "."
        y, x = new_y, new_x
        self.labe_stringx[y][x] = self.nombre
        os.system("cls" if os.name == "nt" else "clear")

print(f'Lo lograste!! {self.nombre},\n Felicidades eres el gran Ganador')