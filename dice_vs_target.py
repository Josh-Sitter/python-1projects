import random
catan=input('Are you playing Settlers of Catan? (Yes=1 No=2):')
try:
    if int(catan) == 1:
        roll=random.randint(2,12)
        if int(roll) == 7:
            print('You rolled a 7, move the robber to a new space, don\'t forget to steal a card')
        else:
            print('You rolled a:',int(roll))
    elif int(catan) == 2:
        print('Sorry, this is only for Settlers of Catan')
    else:
        print('Please enter 1 or 2')
except:
    print('please enter the number 1 or 2')