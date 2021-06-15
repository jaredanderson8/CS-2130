#by Jared Anderson
#Expected Output:
#Without switching:
#33265 / 100000 wins
#33.0% chance to win
 
#With switching:
#66735 / 100000 wins
#66.0% chance to win

import random

i = 0

win = 0
choose = 0
monty = 0;
runs = 100000
x = 0
y = 0
while i < runs:
    doors = [0,1,2]
    
    win = random.choice(doors)
    choose = random.choice(doors)
    
    doors.remove(win)
    if choose in doors:
        doors.remove(choose)
    
    monty = random.choice(doors)
    
    doors = [0,1,2]
    
    doors.remove(monty)
    
    #print("win: " + str(win))
    #print("choose: " + str(choose))
    #print("monty: " + str(monty))
    #print(" ")
    
    if win is choose:
        x = x + 1
    else:
        y = y + 1
     
    i = i + 1
    
print("Without switching:")
print(str(x) + " / " + str(runs) + " wins")
print(str(round((x * 100)/runs), 2) + "% chance to win")


print(" ")

print("With switching:")
print(str(y) + " / " + str(runs) + " wins")
print(str(round((y * 100)/runs), 2) + "% chance to win")
