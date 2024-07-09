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

choices = [rock, paper, scissors]

computer = random.randint(0, 2)

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(f"You chose:\n{choices[player]}")
print("Computer chose:\n" + choices[computer])

if player == computer:
    print("It's a draw!")
elif player == 0 and computer == 2:
    print("You win!")
elif player == 0 and computer == 1:
    print("You lose!")
elif player > computer:
    print("You win!")
elif player < computer:
    print("You lose!")
else:
    print("You typed an invalid number, you lose!")