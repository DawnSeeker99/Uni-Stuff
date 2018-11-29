results =[]
wins = 0
draws = 0
losses = 0
games_played = 5

team_name = input("Enter name of the team: ").capitalize()

for results_left in range(5):
    while True:
        try:
            goals_scored = int(input('How many goals did they score in match {}? '.format(results_left + 1)))
            if goals_scored >= 0:
                goals_against = int(input('How many goals were scored against them in match {}? '.format(results_left + 1)))
                if goals_against >= 0:
                    result = [goals_scored, goals_against]
                    results.append(result)
                    break
                else:
                    print('Enter a positive number.')
            else:
                print('Enter a positive number.')
        except ValueError:
            print('That is not a valid entry.')

for each in list(results):
    if each[0] > each[1]:
        wins += 1
    elif each[0] == each[1]:
        draws += 1
    else:
        losses += 1

points = wins * 3 + draws

print()
print(team_name)
print('{:<8}{:<}'.format('Wins:', wins))
print('{:<8}{:<}'.format('Draws:', draws))
print('{:<8}{:<}'.format('Losses:', losses))
print('{:<8}{:<}'.format('Points:', points))
