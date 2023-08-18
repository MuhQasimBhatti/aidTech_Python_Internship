import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while attempts<11:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

if __name__ == "__main__":
    while guess_number():
        pass

print("Thank you for playing!")
