def pluralise(v):
    if v != 1:
        return 's'
    else:
        return ''

for x in range(10, 0, -1):
    print(str(x), 'green bottle' + pluralise(x), 'sitting on the wall,')
    print(str(x), 'green bottle' + pluralise(x), 'sitting on the wall,')
    print('And if 1 green bottle should accidentally fall,')
    print('There’ll be', str(x-1), 'green bottle' + str(pluralise(x-1)), 'sitting on the wall.\n')
