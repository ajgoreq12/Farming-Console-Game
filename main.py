import random
import time
import os
import keyboard
import os

from Field import Field

cmd = 'mode 120, 41'
os.system(cmd)


#   Options

field_grow_1 = bytes([176]).decode("cp437")
field_grow_2 = bytes([177]).decode("cp437")
field_grow_3 = bytes([178]).decode("cp437")

width = 120
height = 40

#   Fields

fields = [
    Field(0, True),
    Field(1, False),
    Field(2, False),
    Field(3, False),
    Field(4, False),
    Field(5, False),
]
fields[0].plots[0][1][1] = 1
fields[0].plots[1][1][1] = 1

print(fields[0].plots[0])




#   Player Stats

money = 1000
ownedFields = [0,1]
machines = [{"name":"combine", "lvl":1}]

#   Code

name = input("Enter your nickname: ")
os.system('cls')

goodOption = True

while goodOption:

    difficulty = int(input("1 - easy\n"+
                        "2 - normal\n"+
                        "3 - hard\n"+
                        "Choose your difficulty: "))
    os.system('cls')

    if difficulty != 1 and difficulty != 2 and difficulty != 3:
        print("Choose correct option!")
        time.sleep(2)
        os.system('cls')
        
    else:
        goodOption = False
        
if difficulty == 1:
    money = 5000
    ownedFields = [1, 2, 3]
    machines = [{"name":"combine", "lvl":2}]

if difficulty == 3:
    money = 750
    ownedFields = [1]
    machines = [{"name":"combine", "lvl":0}]

for elem in ownedFields:
        fields[elem-1].isOwned = True
        
#   Functions       

def drive():
    for y in range(height):
        for x in range(width):
            if y == 0 or y == height - 1:
                print("-", end="")
            elif x == 0 or x == width - 1 or x == 31 or x == width - 32:
                print("|", end="")
            else:
                print(" ", end="")    
    print()

skip = 0


def fieldDraw(x,y,fieldNr, posX, posY, field_draw_height):
            if x == posX and y == posY:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
            elif x == posX and y == posY+1:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
            elif x == posX and y == posY+2:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
                        
            elif x == posX and y == posY+3:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
            
            elif x == posX and y == posY+4:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
            
            elif x == posX and y == posY+5:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
                        
            elif x == posX and y == posY+6:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
                        
            elif x == posX and y == posY+7:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
            
            elif x == posX and y == posY+8:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
                        
            elif x == posX and y == posY+9:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(0, end="")
                    else:
                        print(2, end="")
            
            
            else:
                skip = 0
            
            return skip
            

# ---Menu Texts
texts = ["HELP", "FIELDS", "OPTIONS"]

field_draw_height = -2




#   Code

for y in range(height):
        field_draw_width = 0
        
        for x in range(width):
            if skip != 0:
                skip -= 1
                continue
            
            # ---Field Draw
            returnFunc = fieldDraw(x,y,0,10,2,field_draw_height)
            skip += returnFunc
            
            returnFunc = fieldDraw(x,y,1,30,2,field_draw_height)
            skip += returnFunc
            
            
            
            
            # ---Menu Draw
            
            if x == 12 and y == 38:
                print(texts[0], end="")
                skip = len(texts[0])-1
                
            elif (x == 10 or x == 21) and y in [38,36,34,32,30]:
                print("|", end="") 
                
            # ---Box Draw
            elif y == 0 or y == height - 1:
                print("-", end="")
    
            elif x == 0 or x == width - 1:
                print("|", end="")

            
                    
            # ---Empty Draw
            else:
                print(" ", end="")
        field_draw_height += 1
print()

for y in fields[0].plots: 
    for x in y:
        pass






input()