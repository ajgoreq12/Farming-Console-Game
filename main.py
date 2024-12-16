import random
import time
import os
import keyboard

from Field import Field

cmd = 'mode 120, 41'
os.system(cmd)


#   Options

field_grow_0 = "\u2588"
field_grow_1 = bytes([176]).decode("cp437")
field_grow_2 = bytes([177]).decode("cp437")
field_grow_3 = bytes([178]).decode("cp437")

width = 120
height = 40

#   Time

Year = 2000
Month = 1
day = 1

monthsSkip = 1

#   Fields

fields = [
    Field(0, True),
    Field(1, False),
    Field(2, False),
    Field(3, False),
    Field(4, False)
]
#fields[0].plots[0][1][1] = 3
#fields[0].plots[1][1][1] = 3

#print(fields[0].plots[0])




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
    ownedFields = [0, 1, 2]
    machines = [{"name":"combine", "lvl":2}]

if difficulty == 3:
    money = 750
    ownedFields = [0]
    machines = [{"name":"combine", "lvl":0}]

for elem in ownedFields:
        fields[elem-1].isOwned = True
        
#   Fancy Functions       

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
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
                        
            
            elif x == posX and y == posY+1:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
            elif x == posX and y == posY+2:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
                        
            elif x == posX and y == posY+3:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
            
            elif x == posX and y == posY+4:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
            
            elif x == posX and y == posY+5:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
                        
            elif x == posX and y == posY+6:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
                        
            elif x == posX and y == posY+7:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
            
            elif x == posX and y == posY+8:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
                        
            elif x == posX and y == posY+9:
                for plots in fields[fieldNr].plots[field_draw_height]:
                    skip = len(fields[fieldNr].plots[field_draw_height])
                    if plots[1] == 0: 
                        print(field_grow_0, end="")
                        
                    elif plots[1] == 1: 
                        print(field_grow_1, end="")
                    
                    elif plots[1] == 2: 
                        print(field_grow_2, end="")
                    
                    elif plots[1] == 3: 
                        print(field_grow_3, end="")
            
            
            else:
                skip = 0
            
            return skip
            
def mainMenu():
    # ---Menu Texts
    texts = ["HELP", "FIELDS", "MACHINES", "SKIP", "ACTIONS", "BUY"]
    fields_nr_text = ["Field nr"]
    skip = 0
    field_draw_height = -2
    for y in range(height):
            field_draw_width = 0
            
            for x in range(width):
                if skip != 0:
                    skip -= 1
                    continue
                
                # ---Field Draw
                if 0 in ownedFields:
                    if x == 10 and y == 1:
                        print("Field num: 1", end="")
                        skip += len("Field num: 1")
                    returnFunc = fieldDraw(x,y,0,11,2,field_draw_height)
                    skip += returnFunc
                
                if 1 in ownedFields:
                    if x == 31 and y == 1:
                        print("Field num: 2", end="")
                        skip += len("Field num: 2")
                    returnFunc = fieldDraw(x,y,1,32,2,field_draw_height)
                    skip += returnFunc
                
                if 2 in ownedFields:
                    if x == 52 and y == 1:
                        print("Field num: 3", end="")
                        skip += len("Field num: 3")
                    returnFunc = fieldDraw(x,y,2,53,2,field_draw_height)
                    skip += returnFunc
                
                if 3 in ownedFields:
                    if x == 73 and y == 1:
                        print("Field num: 4", end="")
                        skip += len("Field num: 4")
                    returnFunc = fieldDraw(x,y,3,74,2,field_draw_height)
                    skip += returnFunc
                
                if 4 in ownedFields:
                    if x == 94 and y == 1:
                        print("Field num: 5", end="")
                        skip += len("Field num: 5")
                    returnFunc = fieldDraw(x,y,4,95,2,field_draw_height)
                    skip += returnFunc
                
                
                
                
                # ---Menu Draw
                
                if x == 11 and y == 38:
                    print(texts[0], end="")
                    skip = len(texts[0])-1
                elif x == 20 and y == 38:
                    print("H", end="")
                    
                elif x == 11 and y == 36:
                    print(texts[2], end="")
                    skip = len(texts[2])-1
                elif x == 20 and y == 36:
                    print("Q", end="")
                
                elif x == 11 and y == 34:
                    print(texts[3], end="")
                    skip = len(texts[3])-1
                elif x == 20 and y == 34:
                    print("E", end="")
                
                elif x == 11 and y == 32:
                    print(texts[4], end="")
                    skip = len(texts[4])-1
                elif x == 20 and y == 32:
                    print("R", end="")
                
                elif x == 11 and y == 30:
                    print(texts[5], end="")
                    skip = len(texts[5])-1
                elif x == 20 and y == 30:
                    print("T", end="")
                    
                    
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

def buyMenu():
    for y in range(height):
            for x in range(width):
                
                
                
                # ---Box Draw
                if y == 0 or y == height - 1:
                    print("-", end="")
        
                elif x == 0 or x == width - 1:
                    print("|", end="")

                # ---Empty Draw
                else:
                    print(" ", end="")
    print()

def actionMenu():
    for y in range(height):
            for x in range(width):
                
                
                
                # ---Box Draw
                if y == 0 or y == height - 1:
                    print("-", end="")
        
                elif x == 0 or x == width - 1:
                    print("|", end="")

                # ---Empty Draw
                else:
                    print(" ", end="")
    print()
    
def skipMenu(monthsSkip):
    
    skip = 0
    for y in range(height):
            for x in range(width):
                if skip != 0:
                    skip -= 1
                    continue
                
                
                # ---Box Draw
                if y == 0 or y == height - 1:
                    print("-", end="")
        
                elif x == 0 or x == width - 1:
                    print("|", end="")
                
                # ---skipOpt
                elif x == 10 and y == 1:
                    print(f"Months skip: {monthsSkip}", end="")
                    skip += len(f"Months skip: {monthsSkip}")-1
                  
                elif x == 10 and y == 2:
                    print(f"Press Q to add 1 month  |   Press E to delete 1 month", end="")
                    skip += len(f"Press Q to delete 1 month  |   Press E to add 1 month")-1

                
                # ---Empty Draw
                else:
                    print(" ", end="")
                
                
    print()
    
    if keyboard.is_pressed('/'):
        inMenu = False
    
def machinesMenu():
    for y in range(height):
            for x in range(width):
                
                
                
                # ---Box Draw
                if y == 0 or y == height - 1:
                    print("-", end="")
        
                elif x == 0 or x == width - 1:
                    print("|", end="")

                # ---Empty Draw
                else:
                    print(" ", end="")
    print()

def helpMenu():
    for y in range(height):
            for x in range(width):
                
                
                
                # ---Box Draw
                if y == 0 or y == height - 1:
                    print("-", end="")
        
                elif x == 0 or x == width - 1:
                    print("|", end="")

                # ---Empty Draw
                else:
                    print(" ", end="")
    print()





#   Game SetUp


inMenu = True
inGame = True

currentSite = "mainMenu"

mainMenu()
while inGame:
    while currentSite == "mainMenu":
        if keyboard.is_pressed('t'):
            os.system(cmd)
            buyMenu()
            currentSite = "buyMenu"
            
        elif keyboard.is_pressed('r'):
            os.system(cmd)
            actionMenu()
            currentSite = "actionMenu"
            
        elif keyboard.is_pressed('e'):
            os.system(cmd)
            skipMenu(monthsSkip)
            currentSite = "skipMenu"
            
        elif keyboard.is_pressed('q'):
            os.system(cmd)
            machinesMenu()
            currentSite = "machinesMenu"

        elif keyboard.is_pressed('h'):
            os.system(cmd)
            helpMenu()
            currentSite = "helpMenu"

    while currentSite =="skipMenu":
        if keyboard.is_pressed('esc'):
            os.system(cmd)
            mainMenu()
            currentSite = "mainMenu"
        elif keyboard.is_pressed('e'):
            os.system(cmd)
            monthsSkip += 1
            skipMenu(monthsSkip)
        elif keyboard.is_pressed('q'):
            if monthsSkip > 1:
                os.system(cmd)
                monthsSkip -= 1
                skipMenu(monthsSkip)
                