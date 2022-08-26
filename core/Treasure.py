print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

print(" You're at cross road now. Try to go left or right ")

choice1 = input("Choose the direction left or right ").lower()

if choice1 == "left":
    choice2 = input("You're at river now.Choose wait to wait until boat arrives or choose swim to jump and swim ").lower()
    if choice2 == "wait":
        choice3 = input(" Boat arrived to another end. There are 3 doors. (Blue, Yellow, Red). Choose one door ").lower()
        if choice3 == "yellow":
            print(" You win !. Treasure is yours")
        elif choice3 == "red":
            print(" Burred by fire, Game over")
        elif choice3 == "blue":
            print(" Eaten by beasts, Game Over")
        else:
            print(" Game Over")
    else:
        print(" Attacked by trout, Game over")
else:
    print(" Fall into a hole, Game Over")