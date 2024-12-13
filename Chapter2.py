# Exercise 2
name=input('Enter your name:')
print('Hello ' + name)

# Exercise 3
Hours=input('Enter Hours:')
Rate=input('Enter Rate:')
Pay = int(Hours) * float(Rate)
print('Pay:', Pay)

# Exercise 4
width = 17
height = 12.0
answer1=(width//2)
answer2=(width/2.0)
answer3=(height/3)
answer4=(1 + 2 * 5)

print(answer1)
a=type(answer1)
print(a)

print(answer2)
b=type(answer2)
print(b)

print(answer3)
c=type(answer3)
print(c)

print(answer4)
d=type(answer4)
print(d)

# Exercise 5
celsius=input('What is the tempurature in celsius?')
fahrenheit=(int(celsius) * 1.8 + 32)
print('Temperature in fahrenheit:', fahrenheit)