import random
import time
import os
import keyboard
import os

from Field import Field

cmd = 'mode 120, 41'
os.system(cmd)


#   Options

width = 120
height = 40

#   Fields

fields = [
    Field(1, False),
    Field(2, False),
    Field(3, False),
    Field(4, False),
    Field(5, False),
    Field(6, False),
]

#   Player Stats

money = 1000
ownedFields = [1, 2]
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
    



#   Code

for y in range(height):
        for x in range(width):
            
            # ---Menu Content
            help = "help"
            
            
            # ---Box Draw
            if y == 0 or y == height - 1:
                print("-", end="")
    
            elif x == 0 or x == width - 1:
                print("|", end="")

            # ---Menu Draw
            
            
            
            elif x == 12 and y == 38:
                print("H", end="")
            elif x == 13 and y == 38:
                print("E", end="")
            elif x == 14 and y == 38:
                print("L", end="")
            elif x == 15 and y == 38:
                print("P", end="")
                
            elif (x == 10 or x == 21) and y in [38,36,34,32,30]:
                print("|", end="")    
            # ---Empty Draw
            else:
                print(" ", end="")    
print()















input()