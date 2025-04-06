"""
Stone Paper Scissor
"""

import random

def main():
    match = userWon = computerWon = 0
    choices = ["Stone", "Paper", "Scissor"]

    while True:
        print("GAME START Match -", match + 1)
        print("1. Stone")
        print("2. Paper")
        print("3. Scissor")

        choice = int(input("Enter choice - "))
        if(choice >= 1 and choice <= 3):
            computer = random.randint(1, 3)

            print("User option - ", choices[choice - 1])
            print("Computer option - ", choices[computer - 1])
            print("---")
            if choice == computer:
                print("Draw")

            elif choice == 1 and computer == 2:
                print("Computer won")
                computerWon += 1

            elif choice == 1 and computer == 3:
                print("User won")
                userWon += 1

            elif choice == 2 and computer == 1:
                print("User won")
                userWon += 1

            elif choice == 2 and computer == 3:
                print("Computer won")
                computerWon += 1

            elif choice == 3 and computer == 1:
                print("Computer won")
                computerWon += 1

            elif choice == 3 and computer == 2:
                print("User won")
                userWon += 1
            print("---")
            match += 1

            print("USER POINTS - ", userWon)
            print("COMPUTER POINTS - ", computerWon)
        else:
            print("**INVALID**")
        
        print("---------------------------------")
        

if __name__ == "__main__":
    main()