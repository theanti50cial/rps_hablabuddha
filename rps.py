# This is a Rock Paper Scissior Game

import random


print("Hello there! Welcome to The Rock Paper Scissors game by HablaBuddha.")

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
---'   ____)____
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

#Write your code below this line 👇

game_images = [rock, paper, scissors]


choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n>> "))
if choice >= 3 or choice < 0:
    print("You typed an invalid number, You lose!")
else:
    print(game_images[choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[computer_choice])

    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice > choice:
        print("You lose!")
    elif choice > computer_choice:
        print("You win!")
    elif computer_choice == choice:
        print("It's a Draw!")

