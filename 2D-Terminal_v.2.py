import time

for Time in range(3):
    print("Loading.  ", end="\r")
    time.sleep(0.5)
    print("Loading.. ", end="\r")
    time.sleep(0.5)
    print("Loading...", end="\r")
    time.sleep(0.5)
print("Done!      ", end="\r")
time.sleep(0.5)
print("                  ")


player_x=1
player_y=27
counter=0
key = False
import random

room_x = range(55,72)
room_y = range(4,9)

def randomizer():
    objective_x = random.randint(1, len(world[0])-2)
    objective_y = random.randint(1, len(world)-2)
    while True:
        if world[objective_y][objective_x] == "■" or (objective_y == player_y and objective_x == player_x) or (objective_x in room_x and objective_y in room_y):
            objective_x = random.randint(1, len(world[0])-2)
            objective_y = random.randint(1, len(world)-2)
        else:
            break
    return objective_x, objective_y

#Tresure Room Area: (x,y) = (55-71,4-8) top left:(55,4) bottom right:(71,8)

world=[
    list("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"),
    list("■.................................................................................■"),
    list("■.................................................................................■"),
    list("■...................■.................................■■■■■■■■■■■■■■■■■■■.........■"),
    list("■.......■■■.........■..........■■■■■■■................■.......■.........■.........■"),
    list("■...................■.................................■....■..■.........■.........■"),
    list("■...................■.................................■....■.......■■■■■■.........■"),
    list("■...................■.......■■■■■■■■■■■■■■■■■■■■■.....■....■■■■■■.......■.........■"),
    list("■...................■.................................■.........■....♦..■.........■"),
    list("■.....................................................■■■■■■■■■Π■■■■■■■■■.........■"),
    list("■..................................■■■■■■........■................................■"),
    list("■....■■■■■■■■■■■■................................■................................■"),
    list("■................................................■.............■..................■"),
    list("■.....................■■■■.......................■.............■..................■"),
    list("■.............■..............■...................■..........■■■■■■■■■■■■■.........■"),
    list("■.............■..............■....................................................■"),
    list("■.............■..............■....................................................■"),
    list("■............................■.........■■■■■■■■■■■■■■■■■■■■■■■....................■"),
    list("■.....■■■■■■.................■....................................................■"),
    list("■.................................................................................■"),
    list("■.................................................................................■"),
    list("■.........................................■■■■■■■■■■..............................■"),
    list("■..................■■■■■■■■■..............■....................■■■■...............■"),
    list("■.........................................■.......................................■"),
    list("■........■................................■.......................................■"),
    list("■........■................................■.......................................■"),
    list("■........■.......................................................■■■■■■■■■........■"),
    list("■........■........................................................................■"),
    list("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"),
]
#====================================================================================

#Starter Random System

objective_x, objective_y = randomizer()
    
#====================================================================================

while True:
    print(f"Stars collected: {counter}/10")

#World Render System
    for row_index, row in enumerate(world):
        for pixel_index, pixel in enumerate(row):
            if pixel_index == player_x and row_index == player_y:
                print("●", end="")
            elif pixel_index == objective_x and row_index == objective_y:
                print("*", end="")
            else:
                print(pixel, end="")
        print()

    print("  w/a/s/d to move    Please press Enter after each input")

#====================================================================================
    move=input(":")

#Control System

    match move:
        case "w":
            player_y-=1
            if world[player_y][player_x]==("■"):
                player_y+=1
            elif world[player_y][player_x]==("Π"):
                if key == False:
                    player_y+=1
                    print("You need a key!")
        case "a":
            player_x-=1
            if world[player_y][player_x]==("■"):
                player_x+=1
            elif world[player_y][player_x]==("Π"):
                if key == False:
                    player_x+=1
        case "s":
            player_y+=1
            if world[player_y][player_x]==("■"):
                player_y-=1
            elif world[player_y][player_x]==("Π"):
                if key == False:
                    player_y-=1
        case "d":
            player_x+=1
            if world[player_y][player_x]==("■"):
                player_x-=1
            elif world[player_y][player_x]==("Π"):
                if key == False:
                    player_x-=1

#====================================================================================

#In Game Random System

    if player_y == objective_y and player_x == objective_x:
        counter+=1
        objective_x, objective_y = randomizer()

#====================================================================================

    if counter >= 10:
        world[14][39]="K"

    if world[player_y][player_x]=="K":
        key = True
        print("You found a key!")
    
    if key == True:
        world[14][39]="."

    if world[player_y][player_x]=="♦":
        print("You Win!")
        break

