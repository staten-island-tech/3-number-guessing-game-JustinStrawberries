import random
random = random.randint(1,10)

number = int(input("Guess the number 1-10: "))

guess_history = []
guess_history.append(number)

while number != random:
    print("Last guesses were", guess_history)
    number = int(input("Try Again: "))
    guess_history.append(number)
    if number == random:
        print("Your guesses were", guess_history)
        print(number, "was correct!")