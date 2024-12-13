max=None
min=None
print('Enter as many numbers as you want, when you say "done" I will tell you your biggest number and your smallest number!')
while True:
    line = input('> ')

    if line == 'done':
        break
    try:
        number = int(line)
        if max is None or number > max:
            max = number
        if min is None or number < min:
            min = number

    except:
        print("Invalid input")
print('Biggest Number:',max)
print('Smallest Number:',min)