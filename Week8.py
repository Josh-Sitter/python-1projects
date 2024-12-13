#Problem 1
name=input('What is your name?')
age=input('What is your age?')
print(name,'is',age,'years old!')

#Problem 2
try:
    num_1=int(input('Enter your first number'))
    num_2=int(input('Enter your second number'))
    num_3=int(input('Enter your third number'))
    if num_1 > num_2 and num_1 > num_3:
        print(num_1,'is the greatest number')
    elif num_2 > num_1 and num_1 > num_3:
        print(num_2,'is the greatest number')
    else:
        print(num_3,'is the greatest number')
except:
    print('You must enter a number')

#Problem 3 need help on this one
def print_args(int3, int2, int3):
    num1=input('enter first value ')
    num2=input('enter second value ')
    num3= input('enter third value ')
    print('Printing Values')
    print(num1)
    print(num2)
    print(num3)
print_args()

#Problem 4
try:
    num1=int(input('Enter your first number'))
    num2=int(input('Enter your second number'))
    num3=int(input('Enter your third number'))
    num4=int(input('Enter your fourth number'))
    num5=int(input('Enter your fifth number'))
    sum=num1+num2+num3+num4+num5
    print('You total is', sum)
except:
    print('please enter a numeric value')

#Problem 5
try:
    num1=int(input('Enter your first number'))
    num2=int(input('Enter your second number'))
    num3=int(input('Enter your third number'))
    num4=int(input('Enter your fourth number'))
    num5=int(input('Enter your fifth number'))
    product=num1*num2*num3*num4*num5
    print('The product is',product)
except:
    print('please enter a numeric value')

 #Problem 6
try:
    num1=int(input('Enter your first number'))
    num2=int(input('Enter your second number'))
    res=print(num1-num2,num1+num2)
except:
    print('Please enter a numeric value')

#Problem 7

#Problem 8

#Problem 9

#Problem 10
try:
    num=int(input('Enter a number'))
    if num>13 and num<40:
        print('That is a good number')
    else:
        print('That is a bad number')
except:
    print('please enter a numeric value')