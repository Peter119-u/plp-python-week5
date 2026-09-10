secret_number = 7
attempts = 0

print("Guess the secret number between 1 and 20!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        break

print(f"You got it in {attempts} tries!")
Test example

A full game could look like this:

Guess the secret number between 1 and 20!
Enter your guess: 15
Too high!
Enter your guess: 3
Too low!
Enter your guess: 7
Congratulations! You guessed it!
You got it in 3 tries!

Notice that:

attempts += 1

increases the counter after every guess.

And:

break
