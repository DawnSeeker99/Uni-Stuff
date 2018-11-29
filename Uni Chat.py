from random import choice
from random import randint


def rand_name():
    NAMES = ['David', 'Chris', 'Jenna', 'Alex', 'Peter']
    return choice(NAMES)


def rand_response():
    RESPONSE = ['Maybe', 'Tell me more', 'I am pleased to hear that', 'I can\'t help you with that', 'I agree']
    return choice(RESPONSE)


def domain_check(email,domain):
    if email.count('@') != 1:
        return False

    if email.find('@') == 0:
        return False

    if not email.endswith(domain):
        return False

    else:
        return True


def extract_name(email):
    return email[0:email.find('@')].capitalize()


def str_in_query(string,query):
    return string.lower() in query.lower()


def random_disconnect():
    chance = randint(1, 100)
    if chance <= 0:
        print('Connection lost...')
        exit()


user_email = input('Enter your university email address: ')

if domain_check(user_email, '@pop.ac.uk') == 0:
    print('Invalid email entered, please use your @pop.ac.uk email address.'
          '\nExiting...')
    exit()
else:
    print('Valid email. Connecting you to an operator.\n')

student_name = extract_name(user_email)
operator_name = rand_name()

print('My name is', operator_name, 'how can I help you today?')

while True:
    x = input('Hi {}, what can I help you with today? '.format(student_name)).lower()

    if x == 'goodbye':
        print('Thank you for using our Online Chat. Goodbye.')
        exit()

    elif str_in_query('library', x):
        print('The library is closed today.')
        random_disconnect()

    elif str_in_query('wifi', x):
        print('WiFi is excellent across campus.')
        random_disconnect()

    elif str_in_query('deadline', x):
        print('Your deadline has been extended by two days.')
        random_disconnect()

    else:
        print(rand_response())
        random_disconnect()

