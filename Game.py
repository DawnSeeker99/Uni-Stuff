import random
gold = 0
virtue = 0
life = 3

name = input('Please enter your name: ').capitalize()

gender = None
while gender not in ('M', 'F'):
    gender = input('What is your gender? Simply enter M or F: ').upper()
    if gender == 'M':
        break
    elif gender == 'F':
        break
    else:
        print('Please enter M or F.')

if gender == 'M':
    hero_name = 'Lord ' + name

if gender == 'F':
    hero_name = 'Lady ' + name

class_1 = None
while class_1 not in ('W', 'K', 'A'):
    class_1 = input('Now then, it is time to choose your class. Please enter W (Wizard), K (Knight) or A (Assassin): ').upper()
    if class_1 == 'W':
        break
    if class_1 == 'K':
        break
    if class_1 == 'A':
        break
    else:
        print('Please enter W, K or A.')

print('Then rise, ' + hero_name + '.')
if class_1 == 'W':
    print('You have chosen to be a wizard!')
if class_1 == 'K':
    print('You have chosen to be a knight!')
if class_1 == 'A':
    print('You have chosen to be an assassin!')

print('Now then, it is time to start your new journey!')
print('You begin in the small town of ..., there are two directions you could go. Do you want to go East or West?')
direction_1 = None
while direction_1 not in ('E', 'W'):
    direction_1 = input('Please enter E (East) or W (West): ').upper()
    if direction_1 == 'E':
        break
    if direction_1 == 'W':
        break
    else:
        print('Please enter E or W.')

if direction_1 == 'E':
    print('You leave the village by the East exit.')
    print('Whilst walking along the path you fall into a bog.')
    obstacle_1 = None
    obstacle_1 = input('Do you 1 (Flail around), 2 (Try to grab the tree branch next to you pull yourself out) or 3 (Spread your body weight out and wait for someone to save you)?: ')

    if obstacle_1 == '1':
            survive_1 = random.randint(0, 4)
            if survive_1 == 0:
                print('Somehow, despite everything you have been told, you survive.')
            elif survive_1 > 0:
                print('You flail around for a few minutes, slowly sinking into the bog.')
                life = life - 1
                print('You died. you now have', life, 'lives left.')
                if life == 0:
                    print('You have lost all of your lives.')
                    exit()

    if obstacle_1 == '2':
        survive_2 = random.randint(0, 2)
        if survive_2 == 0:
            print('You manage to pull yourself out of the bog.')
        elif survive_2 > 0:
            print('The branch snaps, leaving your to fall into the bog.')

            obstacle_2 = None
            obstacle_2 = input('Do you want to 1 (Flail around) or 2 (Spread your body weight out and wait for someone to save you)?: ')
            if obstacle_2 == '1':
                survive_2 = random.randint(0, 6)
                if survive_2 == 0:
                    print('Somehow, despite everything you have been told, you survive.')
                elif survive_2 > 0:
                    print('You flail around for a few minutes, slowly sinking into the bog.')
                    life = life - 1
                    print('You died. you now have', life, 'lives left.')
                    if life == 0:
                        print('You have lost all of your lives.')
                        exit()

            if obstacle_2 == '2':
                print('You relax and enjoy the scenery of the clouds passing you by. Eventually a group of people come by and help you out of the bog.')
                print('Oh no! Your rescuers are bandits! You\'ll have to fight them!')

                if class_1 == 'A':
                    fight_1 = random.randint(0, 6)
                    if fight_1 == 0:
                        print('You manage to defeat your attackers. You then decide to loot them.')
                        gold = gold + 13
                        print('You manage to find Gold.')
                        print('You now have', gold, 'Gold.')
                    elif fight_1 > 0:
                        print('Due to your inability to fight large groups, you fail to stave off your attackers.')
                        life = life - 1
                        print('You died. you now have', life, 'lives left.')
                        if life == 0:
                            print('You have lost all of your lives.')
                            exit()

                if class_1 == 'W':
                    fight_1 = random.randint(0, 3)
                    if fight_1 == 0:
                        print('You manage to defeat your attackers.')

                    if fight_1 > 0:
                        fight_1_1 = input('You start to struggle, do you want to 1 (Run away) or 2 (Continue to fight)?: ')

                        if fight_1_1 == '1':
                            run_away_1 = random.randint(0,1)
                            if run_away_1 == 0:
                                print('You manage to run away.')
                            elif run_away_1 > 0:
                                print('Your attempt to run fails.')
                                life = life - 1
                                print('You died. you now have', life, 'lives left.')
                                if life == 0:
                                    print('You have lost all of your lives.')
                                    exit()

                        if fight_1_1 == '2':
                            fight_1_1_2 = random.randint(0, 6)
                            if fight_1_1_2 == 0:
                                print('You manage to defeat all of your attackers. You then decide to loot them.')
                                gold = gold + 13
                                print('You manage to find Gold.')
                                print('You now have', gold, 'Gold.')
                            elif fight_1_1_2 > 0:
                                print('You put up a valiant fight, but in the end your are overwhelmed.')
                                life = life - 1
                                print('You died. you now have', life, 'lives left.')
                                if life == 0:
                                    print('You have lost all of your lives.')
                                    exit()

                if class_1 == 'K':
                    fight_1 = random.randint(0, 1)
                    if fight_1 == 0:
                        print('You manage to defeat your attackers.')
                        print('You manage to defeat all of your attackers. You then decide to loot them.')
                        gold = gold + 13
                        print('You manage to find Gold.')
                        print('You now have', gold, 'Gold.')
                    elif fight_1 > 0:
                        print('You put up a valiant fight, but in the end your are overwhelmed.')
                        life = life - 1
                        print('You died. you now have', life, 'lives left.')
                        if life == 0:
                            print('You have lost all of your lives.')
                            exit()



    if obstacle_1 == '3':
        print('You relax and enjoy the scenery of the clouds passing you by. Eventually a group of people come by and help you out of the bog.')
        print('Oh no! Your rescuers are bandits! You\'ll have to fight them!')
        if class_1 == 'A':
            fight_1 = random.randint(0, 6)
            if fight_1 == 0:
                print('You manage to defeat your attackers.')
            elif fight_1 > 0:
                print('Due to your inability to fight large groups, you fail to stave off your attackers.')
                life = life - 1
                print('You died. you now have', life, 'lives left.')
                if life == 0:
                    print('You have lost all of your lives.')
                    exit()

        if class_1 == 'W':
            fight_1 = random.randint(0, 3)
            if fight_1 == 0:
                print('You manage to defeat your attackers.')
            if fight_1 > 0:
                fight_1_1 = input('You start to struggle, do you want to 1 (Run away) or 2 (Continue to fight)?: ')

                if fight_1_1 == '1':
                    run_away_1 = random.randint(0, 1)
                    if run_away_1 == 0:
                        print('You manage to run away.')
                    elif run_away_1 > 0:
                        print('Your attempt to run fails.')
                        life = life - 1
                        print('You died. you now have', life, 'lives left.')
                        if life == 0:
                            print('You have lost all of your lives.')
                            exit()

                    if fight_1_1 == '2':
                        fight_1_1_2 = random.randint(0, 6)
                        if fight_1_1_2 == 0:
                            print('You manage to defeat all of your attackers. You then decide to loot them.')
                            gold = gold + 13
                            print('You manage to find Gold.')
                            print('You now have', gold, 'Gold.')
                        elif fight_1_1_2 > 0:
                            print('You put up a valiant fight, but in the end your are overwhelmed.')
                            life = life - 1
                            print('You died. you now have', life, 'lives left.')
                            if life == 0:
                                print('You have lost all of your lives.')
                                exit()

        if class_1 == 'K':
            fight_1 = random.randint(0, 1)
            if fight_1 == 0:
                print('You manage to defeat your attackers.')
                print('You manage to defeat all of your attackers. You then decide to loot them.')
                gold = gold + 13
                print('You manage to find Gold.')
                print('You now have', gold, 'Gold.')
            elif fight_1 > 0:
                print('You put up a valiant fight, but in the end your are overwhelmed.')
                life = life - 1
                print('You died. you now have', life, 'lives left.')
                if life == 0:
                    print('You have lost all of your lives.')
                    exit()


if direction_1 == 'E':
    print('You continue on into the next village.')
    raid_1 = None
    raid_1 = input('You see a bank, do you want to go and raid it? Enter Y or N: ').upper()
    if raid_1 == 'Y':
        virtue = virtue - 1
        if class_1 == 'K':
            raid_1_1 = random.randint(0, 3)
            if raid_1_1 == 0:
                print('You manage to sneak past all of the guards.')
                gold_1 = random.randint(1, 4)
                gold = gold + gold_1*3
                print('You now have', gold, 'Gold.')
                print('You leave the bank, pretending you didn\'t do anything.')

            elif raid_1_1 > 0:
                print('The guards catch you, they then sentence you to the death penalty.')
                life = life - 1
                print('You died. you now have', life, 'lives left.')
                if life == 0:
                    print('You have lost all of your lives.')
                    exit()

        if class_1 == 'A':
                raid_1_2 = random.randint(0, 1)
                if raid_1_2 == 0:
                    print('You manage to sneak past all of the guards.')
                    gold_1 = random.randint(1, 4)
                    gold = gold + gold_1 * 3 + 3
                    print('You now have', gold, 'Gold.')
                    print('You leave the bank, pretending you didn\'t do anything.')

                elif raid_1_2 > 0:
                    print('The guards catch you, they then sentence you to the death penalty.')
                    life = life - 1
                    print('You died. you now have', life, 'lives left.')
                    if life == 0:
                        print('You have lost all of your lives.')
                        exit()

        if class_1 == 'W':
                raid_1_1 = random.randint(0, 3)
                if raid_1_1 == 0:
                    print('You manage to sneak past all of the guards.')
                    gold_1 = random.randint(1, 4)
                    gold = gold + gold_1 * 3
                    print('You now have', gold, 'Gold.')
                    print('You leave the bank, pretending you didn\'t do anything.')

                elif raid_1_1 > 0:
                    print('The guards catch you, they then sentence you to the death penalty.')
                    life = life - 1
                    print('You died. you now have', life, 'lives left.')
                    if life == 0:
                        print('You have lost all of your lives.')
                        exit()

    if raid_1 == 'N':
        print('You decide to be an upstanding citizen and not raid the bank.')

    else:
        print('Please enter Y or N.')

    attack_1 = None
    while attack_1 not in ('Y', 'N'):
        attack_1 = input('A man attacks you and demands that you give him money (enter Y or N): ').upper()

        if attack_1 == 'Y':
            print('You decide to pay the attacker, you give him 5 Gold')

            if gold >= 5:
                gold = gold - 5
                print(gold)
            elif gold < 5:
                print('You reach into your pockets and find that you do not have enough Gold. The man attacks you.')
                if class_1 == 'W':
                    magic_immunity_2 = random.randint(0, 2)
                    if magic_immunity_2 == 0:
                        print('You find that somehow the enemy is immune to your magic. He manages to defeat you.')
                        life = life - 1
                        print('You died. you now have', life, 'lives left.')
                        if life == 0:
                            print('You have lost all of your lives.')
                            exit()

                    elif magic_immunity_2 > 0:
                        print('You manage to defeat the attacker.')

                if class_1 == 'K':
                    attack_1_1 = random.randint(0, 1)
                    if attack_1_1 == 0:
                        print('You manage to defeat your attacker.')
                    elif attack_1_1 > 0:
                        print('Your attacker manages to get in a good blow. He then finishes you off.')
                        life = life - 1
                        print('You died. you now have', life, 'lives left.')
                        if life == 0:
                            print('You have lost all of your lives.')
                            exit()

                if class_1 == 'A':
                    attack_1_1 = random.randint(0, 4)
                    if attack_1_1 == 0:
                        print('You manage to defeat your attacker.')
                    elif attack_1_1 > 0:
                        print('Your attacker manages to get in a good blow. He then finishes you off.')
                        life = life - 1
                        print('You died. you now have', life, 'lives left.')
                        if life == 0:
                            print('You have lost all of your lives.')
                            exit()

            print('After killing your attacker, you decide to loot him.')
            gold = gold + 4
            print('You now have', gold, 'Gold.')

        elif attack_1 == 'N':
            print('The man attacks you.')

            if class_1 == 'W':
                magic_immunity_2 = random.randint(0, 2)
                if magic_immunity_2 == 0:
                    print('You find that somehow the enemy is immune to your magic. He manages to defeat you.')
                    life = life - 1
                    print('You died. you now have', life, 'lives left.')
                    if life == 0:
                        print('You have lost all of your lives.')
                        exit()

                elif magic_immunity_2 > 0:
                    print('You manage to defeat the attacker.')
                    print('After killing your attacker, you decide to loot him.')

            if class_1 == 'K':
                attack_1_1 = random.randint(0, 1)
                if attack_1_1 == 0:
                    print('You manage to defeat your attacker.')
                    print('After killing your attacker, you decide to loot him.')
                    gold = gold + 13
                    print('You now have', gold, 'Gold.')
                elif attack_1_1 > 0:
                    print('Your attacker manages to get in a good blow. He then finishes you off.')
                    life = life - 1
                    print('You died. you now have', life, 'lives left.')
                    if life == 0:
                        print('You have lost all of your lives.')
                        exit()

            if class_1 == 'A':
                attack_1_1 = random.randint(0, 4)
                if attack_1_1 == 0:
                    print('You manage to defeat your attacker.')
                    print('After killing your attacker, you decide to loot him.')
                    gold = gold + 13
                    print('You now have', gold, 'Gold.')
                elif attack_1_1 > 0:
                    print('Your attacker manages to get in a good blow. He then finishes you off.')
                    life = life - 1
                    print('You died. you now have', life, 'lives left.')
                    if life == 0:
                        print('You have lost all of your lives.')
                        exit()

        else:
            print('Please enter Y or N.')

    print('You go to leave the village, but you see a woman begging for money to feed her children.')
    virtue_1 = None
    while virtue_1 not in ('Y', 'N'):
        virtue_1 = input('Do you wish to give her money? (enter Y or N): ').upper()
        if virtue_1 == 'Y':
            print('You choose to give the woman 3 Gold, she is very grateful.')
            virtue = virtue + 1
        elif virtue_1 == 'N':
            print('You to walk past the woman, not giving her any thought.')
        else:
            print('Please enter Y or N.')


    print('You look around the rest of the village, all you find is a forest and a path heading North.')
    direction_2 = None
    while direction_2 not in ('F' or 'N'):
        direction_2 = input('Do you want to go into the Forest (F) or head North (N)?: ')
        if direction_2 == 'F':
            print('You go into the forest.')
        elif direction_2 == 'N':
            print('You decided to head North')
        else:
            print('Please enter F or N')











if direction_1 == 'W':
    print('You leave the village by the West exit.')
    print('You pass by a man being hassled by what looks to be a thief.')

    fight_2 = None
    fight_2 = input('Do you want to 1 (intervene) or 2 (Walk past)?: ')
    if fight_2 == '1':
        virtue = virtue + 1

        if class_1 == 'W':
            magic_immunity_1 = random.randint(0, 2)
            if magic_immunity_1 == 0:
                print('You find that somehow the enemy is immune to your magic. He manages to defeat you.')
                print('You died.')
            elif magic_immunity_1 > 0:
                print('You manage to defeat the attacker.')

        if class_1 == 'K':
                fight_1 = random.randint(0, 1)
                if fight_1 == 0:
                    print('You manage to defeat the thief, easily overwhelming him.')
                elif fight_1 > 0:
                    print('The thief manages to get in a good blow. He then finishes you off.')
                    print('You died. you now have', life, 'lives left.')
                    life = life - 1
                    if life == 0:
                        print('You have lost all of your lives.')
                        exit()

        if class_1 == 'A':
            print('You sneak up on the target, and defeat him.')

    print('The man is grateful for your help, he rewards you with 5 Gold.')
    gold = gold + 5
    print('You now have', gold, 'Gold.')

if direction_1 == 'W':
    print('You arrive at a village by a lake.')



































