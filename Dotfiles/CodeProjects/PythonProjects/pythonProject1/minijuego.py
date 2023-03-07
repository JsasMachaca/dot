import readchar
import os
from random import randint
from time import sleep

POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 1
my_position = [5, 0]

map_objects = []
end_game = False

new_position = [6, 8]

if new_position not in map_objects and new_position != my_position:
    map_objects.append(new_position)

obstacle_definition = """\
#####  ######      ##
######      #### ####
#######              
########### #     ###
                     
                     
######      #####   #
  #        ####     #
####                 
###                 #
############         
#####     ##         
###      ###    ##   
########        #####
######       #####   \
"""

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while not end_game:

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):

        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                if object_in_cell:
                    print("Inicia el combate")
                    os.system("clear")
                    end_game = True
                    sleep(3)
                    os.system("clear")
                    sleep(3)
                    print("BIENBENIDO EL COMBATE POQUEMON ")
                    os.system("clear")
                    print("Te has encontrado con un maestro pokemon y te ha retado a un duelo")
                    start_combat = input("Presiona enter para aceptar el combate o presiona [q] para salir : ")
                    os.system("clear")
                    if start_combat == "":
                        os.system("clear")
                        print("Has aceptado el combate preparate")
                        titulo_pikachu = "Turno de pikachu"

                        titulo_squirtle = "Turno de squirtle"

                        VIDA_INICIAL_PIKACHU = 100
                        VIDA_INCIAL_SQUIRTLE = 100

                        vida_pikachu = VIDA_INICIAL_PIKACHU
                        vida_squirtle = VIDA_INCIAL_SQUIRTLE

                        while vida_pikachu > 0 and vida_squirtle > 0:
                            # se desenvuelven los turnos del combate

                            # turno de pikachu
                            print(titulo_pikachu + "\n" + "-" * len(titulo_pikachu))
                            ataque_pikachu = randint(1, 2, )
                            if ataque_pikachu == 1:
                                print("Pikachu ataca con bola voltio")
                                vida_squirtle -= 10
                            elif ataque_pikachu == 2:
                                print("Pikachu ataca con onda trueno")
                                vida_squirtle -= 11

                            else:
                                print("Pikachu descansa")

                            if vida_squirtle < 0:
                                vida_squirtle = 0

                            if vida_pikachu < 0:
                                vida_pikachu = 0

                            barra_de_vida_pikachu = int(10 * vida_pikachu / VIDA_INICIAL_PIKACHU)
                            barra_de_vida_squirtle = int(10 * vida_squirtle / VIDA_INCIAL_SQUIRTLE)
                            print("Pikachu:    [{}]({}/{})".format("*" * barra_de_vida_pikachu, vida_pikachu,
                                                                   VIDA_INICIAL_PIKACHU))
                            print("Squirtle:   [{}]({}/{})".format("*" * barra_de_vida_squirtle, vida_squirtle,
                                                                   VIDA_INCIAL_SQUIRTLE))

                            print("\n")
                            input("Presiona enter para continuar....")

                            os.system("clear")

                            print(titulo_squirtle + "\n" + "-" * len(titulo_squirtle))
                            ataque_squirtle = input(""""Que ataque deseas realizar?
                            P - Placaje
                            A - Pistola de agua
                            B - Burbuja
                            D - Descansar
                            """"")

                            while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "D":
                                ataque_squirtle = input("""Que ataque deseas realizar?
                            P - Placaje
                            A - Pistola de agua
                            B - Burbuja
                            D - Descansar
                            """)

                            if ataque_squirtle == "P":
                                print("Squirtle ataca con Placaje")
                                vida_pikachu -= 10

                            elif ataque_squirtle == "A":
                                print("Squirtle ataca con Pistola de agua")
                                vida_pikachu -= 12

                            elif ataque_squirtle == "B":
                                print("Squirtle ataca con Burbuja")
                                vida_pikachu -= 9

                            elif ataque_squirtle == "D":
                                print("Squirtle descansa")

                            if vida_squirtle < 0:
                                vida_squirtle = 0

                            os.system("clear")

                        print("\n")

                        if vida_squirtle < 0 or vida_squirtle == 0:
                            print("Pikachu gano la guerra!!!!")
                            exit()

                        elif vida_pikachu < 0 or vida_pikachu == 0:
                            print("Squirtle gano la pelea!!!")
                            exit()

                    else:
                        os.system("clear")
                        print("xd?")
                        os.system("clear")

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"
            print(f" {char_to_draw} ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()
    new_position = None
    if direction == "w":

        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":

        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":

        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":

        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        end_game = True
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position
    os.system("clear")


