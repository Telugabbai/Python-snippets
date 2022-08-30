#
# Rules:
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
# 0 for Rock, 1 for Paper and 2 scissors.

from random import randint, choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice1 = int(input(" Enter your choice, 0 for Rock, 1 for Paper and 2 scissors.  "))
rps = [rock, paper, scissors]
machine_input = choice(rps)

print(machine_input)
print("Computer choose :")

if choice1 == 0:
    print(rock)
elif choice1 == 1:
    print(paper)
elif choice1 == 2:
    print(scissors)
else:
    print(" Enter Valid number")

if (machine_input == rock and choice1 == 0) or (machine_input == paper and choice1 == 1) or (machine_input == scissors and choice1 == 2):
    print("Tie")
elif (machine_input == rock and choice1 == 1) or (machine_input == paper and choice1 == 2) or (machine_input == scissors and choice1 == 0):
    print("You won the game")
else:
    print(" You loose the game")