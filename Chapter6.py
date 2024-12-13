#Exercise 4
# Answer: d)

#Exercise 5
# Answer: d)

#Exercise 6
Hours=input('Enter Hours:')
Rate=input('Enter Rate:')
def computepay(hour, rate):
    pay = int(hour) * float(rate)
    print('Pay:', pay)
def computeot(hour, rate):
    Pay = (40 * float(rate)) + ((int(hour)-40) * (1.5 * float(rate)))
    print('Pay:', Pay)
try:
    if int(Hours)<=40:
        computepay(Hours, Rate)
    else:
        computeot(Hours, Rate)
except:
    print('Error, please enter numeric input')