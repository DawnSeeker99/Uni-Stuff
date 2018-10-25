name = input('Please enter the student\'s name: ').capitalize()

while True:
    try:
        test_number = int(input('How many tests did the student take? '))
        if test_number < 0:
            print('Please enter a positive number.')
        else:
            break
    except ValueError:
        print('Please enter a valid number.')

total_marks = 0
for count in range(test_number):
    while test_number:
        try:
            total_marks += int(input('Enter result #' + str(count + 1) + ': '))
            if (count + 1) < 0:
                print('Please enter a positive number below 100.')
            if (count + 1) > 100:
                print('Please enter a positive number below 100.')
            else:
                break
        except ValueError:
            print('Please enter a valid number.')

average_mark = total_marks / test_number

print(name, 'received', average_mark, 'marks on average.')






