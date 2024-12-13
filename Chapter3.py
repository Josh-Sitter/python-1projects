# Exersise 1
Hours=input('Enter Hours:')
Rate=input('Enter Rate:')
if int(Hours)<=40:
    Pay = int(Hours) * float(Rate)
else:
    Pay = (40 * float(Rate)) + ((int(Hours)-40) * (1.5 * float(Rate)))
print('Pay:', Pay)

# Exersise 2
Hours=input('Enter Hours:')
Rate=input('Enter Rate:')
try:
    if int(Hours)<=40:
        Pay = int(Hours) * float(Rate)
    else:
        Pay = (40 * float(Rate)) + ((int(Hours)-40) * (1.5 * float(Rate)))
    print('Pay:', Pay)
except:
    print('Error, please enter numeric input')
# Exersise 3
score=input('Enter score')
if float(score)>=0.0 and float(score)<=1.0:
    if float(score)>=0.9:
        print('A')
    elif float(score)>=0.8:
        print('B')
    elif float(score)>=0.7:
        print('C')
    elif float(score)>=0.6:
        print('D')
    elif float(score)<0.6:
        print('F')
else:
    print('Bad score')