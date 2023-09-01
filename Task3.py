import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Roller App!")

    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice (e.g., 6 for a standard six-sided die): "))
            if num_sides < 2:
                print("Please enter a valid number of sides greater than or equal to 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls < 1:
                print("Please enter a valid number of rolls greater than or equal to 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        print(f"\nRolling a {num_sides}-sided die {num_rolls} times:")
        
        for i in range(num_rolls):
            result = roll_dice(num_sides)
            print(f"Roll {i + 1}: {result}")

        play_again = input("\nDo you want to roll the dice again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for using the Dice Roller App!")
            break  # Exit the play again loop if the user enters anything other than "yes"

if __name__ == "__main__":
    main()
