import random

number = random.randint(0, 100)

while 1:
    try:
        guess = int(input('Please enter your guess: '))
        if guess == number:
            break
        elif guess >= number:
            print('Try a lower number.')

        elif guess <= number:
            print('Try a higher number')
    except ValueError:
        print('Stop trying to break me. Enter a valid number.')

print('Well done, you guessed the number!')




