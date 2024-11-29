import random

options = ("rock", "paper", "scissors")
player = None
computer = None
running = True


while running:

    while player not in options:
        player = input(f"Enter a choice (rock, paper, scissors): ").lower()
        computer = random.choice(options)
    print(f"Player {player}")
    print(f"Computer {computer}")

    if player == computer:
        print(f"Its a tie")
    elif player == "rock" and computer == "scissors":
        print(f"Player wins")
    elif player == "scissors" and computer == "paper":
        print(f"Player wins ")
    elif player == "paper" and computer == "rock":
        print(f"Player wins ")
    else:
        print(f"Computer wins")

    player = None
    computer = None

    if not input(f"Play again? (y/n): ").lower() == "y":
        running = False


print(f"Thanks for playing!")
