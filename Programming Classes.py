while True:
    try:
        number_of_students = int(input('How many students do you have? '))
        if number_of_students <= 0:
            print('Please enter a positive value above zero.')
        else:
            break
    except ValueError:
        print('This is not a valid entry, please enter an integer.')

while True:
    try:
        int(input('How many sweets do you have? '))
        if number_of_students <= 0:
            print('Please enter a positive value above zero.')
        else:
            break
    except ValueError:
        print('This is not a valid entry, please enter an integer.')


