# Number Guessing Game

```Python
secret_number = 22
attempts = 0
while True:
    # Ask for user's guess
    try:
        guess = int(input("Enter a number: "))
    except ValueError:
        print("That's not a valid number.")
        continue
    # Increase attempts
    attempts += 1
    # Check the guess
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct")
        break
print(attempts)
````
