'''
STONE = 1
PAPER = 0
SCISSORS = -1
'''

import random

# ASCII ART

stone = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

computer = random.choice([1, 0, -1])

you = input("Enter PAPER, STONE or SCISSORS: ").upper()

dic = {
    "PAPER": 0,
    "STONE": 1,
    "SCISSORS": -1
}

art = {
    "PAPER": paper,
    "STONE": stone,
    "SCISSORS": scissors
}

if you not in dic:
    print("Invalid choice")

else:

    new = dic[you]

    reverseDic = {
        0: "PAPER",
        1: "STONE",
        -1: "SCISSORS"
    }

    # USER
    print(f"\nYOU CHOSE {you}")
    print(art[you])

    # COMPUTER
    computer_choice = reverseDic[computer]

    print(f"COMPUTER CHOSE {computer_choice}")
    print(art[computer_choice])

    # RESULT

    if computer == new:
        print("It's a draw")

    elif computer == 1 and new == 0:
        print("You win")

    elif computer == 1 and new == -1:
        print("Computer wins")

    elif computer == 0 and new == -1:
        print("You win")

    elif computer == 0 and new == 1:
        print("Computer wins")

    elif computer == -1 and new == 1:
        print("You win")

    elif computer == -1 and new == 0:
        print("Computer wins")