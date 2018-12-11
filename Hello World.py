from math import ceil

while True:
    try:
        students = int(input('How many students are there? '))
        if students > 0:
            break
        else:
            print('Please enter a positive number.')
    except ValueError:
        print('Please enter a positive number')

while True:
    try:
        computers = int(input('How many computers are there in each lab? '))
        if computers > 0:
            break
        else:
            print('Please enter a positive number.')
    except ValueError:
        print('Please enter a positive number')

labs = ceil(students/computers)

if students > computers:
    print('You need', labs, 'labs for all the students.')
elif computers >= students:
    print('You need', labs, 'lab for all the students.')
