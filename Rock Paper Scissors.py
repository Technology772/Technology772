import random

scissors = '''
    _______
---'    ____)____
            ______)
        __________)
        (____)
---.____(___)

'''

rock = '''
    _______
---'    ___)
        (___)
        (___)
        (__)
  ---.__(_)

'''

paper = '''

    _______
---'    ____)____
           ______)
           ______)
          _______)
---.___________)

'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2 )

print("computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You Lose !")

elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Its a Draw! ")






