import random

secret_number = random.randint(1, 10)
attempt = 0

print("Guess a number between 1 and 10.")

while True:
    guess = input("Enter your guess: ")

    if not guess.isnumeric():
        print("❌ Invalid input. Please enter a number.")
        attempt += 1
        continue

    guess = int(guess)
    attempt += 1

    if guess < secret_number:
        print("🔻 Too low!")
    elif guess > secret_number:
        print("🔺 Too high!")
    else:
        print(f"🎉 Yes! Your guess is correct. It was {secret_number}.")
        print(f"🧠 You guessed it in {attempt} attempts.")
        break
