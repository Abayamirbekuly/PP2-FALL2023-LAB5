import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

if __name__ == "__main__":
    guess_the_number()
