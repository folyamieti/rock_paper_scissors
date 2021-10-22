import random

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

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

simbols = [rock, paper, scissors]

if player_choice == 0 or player_choice == 1 or player_choice == 2:

    print(simbols[player_choice - 1])

    random_simbol = random.randint(0, 2)

    print(f"Computer chose: \n {simbols[random_simbol]}")

    if (player_choice - 1) == random_simbol:
        print("Nice try, but no winner today!")
    elif (((player_choice - 1) == 0) and random_simbol == 2) or (((player_choice - 1) == 1) and random_simbol == 0) or (
            ((player_choice - 1) == 2) and random_simbol == 1):
        print("You smashed it!")
    else:
        print("It's not your day :(. You've lost!")

else:
    print("You've typed and invalid number. You lose!")


