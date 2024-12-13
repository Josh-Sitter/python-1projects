print('You are stranded on a raft after your boat sunk in the middle of the ocean.')
opt_1=int(input('What would you like to do, 1 Paddle in one direction and hope to find land or 2 Save energy and let the currents take you?'))
if opt_1 == 1:

    print('You found an island.')
    opt_2a=int(input('What would you like to do, 1 Stop at the isnand or 2 keep padding until you find something else?'))
    if opt_2a == 1:
        print('There is a lot of recources on this island.')
        opt_3a=int(input('What would you like to do, 1 Stay until someone finds you or 2 take what you need and keep going?'))
        if opt_3a == 1:
            print('You build a hut on this island and you never get found. :(')
        else:
            print('The resources from the island lasted you long enough that a passing boat found you and you were saved. :)')
    else:
        while opt_2a != 1:
            print('So far you have found nothing!')
            opt_1=int(input('What would you like to do, 1 Paddle in one direction and hope to find land or 2 Save energy and let the currents take you?'))
            if opt_1 == 1:

                print('You found an island.')
                opt_2a=int(input('What would you like to do, 1 Stop at the isnand or 2 keep padding until you find something else?'))
                if opt_2a == 1:
                    print('There is a lot of recources on this island.')
                    opt_3a=int(input('What would you like to do, 1 Stay until someone finds you or 2 take what you need and keep going?'))
                    if opt_3a == 1:
                        print('You build a hut on this island and you never get found. :(')
                    else:
                        print('The resources from the island lasted you long enough that a passing boat found you and you were saved. :)')
        print('You found a boat!')
        opt_3b=int(input('What would you like to do, 1 approach the boat or 2 keep paddling?'))
        if opt_3b == 1:
            print('It was a pirate ship, you were put in the brig and never seen again. :(')
        else:
            print('You never find anything else and die of dehydration. :(')
else:
    print('You find an island with traces of humans.')
    opt_2b=int(input('What would you like to do, 1 explore the island or 2 keep going?'))
    if opt_2b == 1:
        print('The island is a cannabal island and you are taken captive!')
        opt_3c=int(input('What would you like to do, 1 try to fight your way out or 2 try to give them gifts so they release you?'))
        if opt_3c == 1:
            print('You took them by surprise in the middle of the night and made it back to your ship. A passing by boat took you to safty. :)')
        else:
            print('They didnt like your gifts and roast you over a fire. :(')
    else:
        print('Your raft starts to break apart!')
        opt_3d=int(input('What would you like to do, 1 attempt to fix it using your clothes as rope or 2 stay on the biggest piece and keep floating?'))
        if opt_3d == 1:
            print('While trying to fix your raft you cut yourself and attract a group of sharks. Your shark bate. :(')
        else:
            print('You get super lucky and float back home. :)')