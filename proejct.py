import random
random = random.randint(1,10)

number = int(input("Guess the number 1-10: "))

guess_history = []
guess_history.append(number)

while number != random:
    if number > random:
        print("Last guesses were", guess_history)
        number = int(input("Your guess was greater than the number, Try Again: "))
        guess_history.append(number)
    if number < random:
        print("Last guesses were", guess_history)
        number = int(input("Your guess was Less than the number, Try Again: "))
        guess_history.append(number)

if number == random:
    print("Your guesses were", guess_history)
    print(number, "was correct!")