import random
from time import sleep

def rock(b, a):
    if a == b:
        print(f"It's a tie!, The computer chooses also chooses {a}")
    elif a == "paper":
        print(f"You lose! The computer choose {a}.")
    elif a == "scissors":
        print(f"You win! The computer choose {a}.")

def paper(b, a):
    if a == b:
        print(f"It's a tie!, The computer chooses also chooses {a}")
    elif a == "scissors":
        print(f"You lose! The computer choose {a}.")
    elif a == "rock":
        print(f"You win! The computer choose {a}.")

def scissors(b, a):
    if a == b:
        print(f"It's a tie!, The computer chooses also chooses {a}")
    elif a == "rock":
        print(f"You lose! The computer choose {a}.")
    elif a == "paper":
        print(f"You win! The computer choose {a}.")

def computer():
    return random.choice(["rock", "paper", "scissors"])

def play():
    outputs = ["rock", "paper", "scissors"]
    a= computer()
    b = input("Welcome! Enter rock, paper, or scissors: ").lower()

    while True:
        if b not in outputs:
            print("Invalid input. Please enter again")
            sleep(1)
            
        match b:
            case "rock":
                rock(b, a)
            case "paper":
                paper(b, a)
            case "scissors":
                scissors(b, a)
        break   

def play_again():
    while True:
        answer = input("Would you like to play again? ").lower()
        if answer.startswith("y"):
            return True
        if answer.startswith("n"):
            return False
        else:
            print("Please enter 'yes' or 'no'.")
            sleep(1)

play() 

while True:
    if play_again():
        play()
    else:
        print("Thank you for playing! Hope to see you again!")
        break