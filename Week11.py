# Excercise 1
fruit = 'banana'
index = 0
counter = 0
while counter < len(fruit):
    letter = fruit[index-1]
    print (letter)
    index = index - 1
    counter = counter + 1

# Excercise 2
# fruit[:] would print the whole value of fruit because it is not given when to start or end.

#Excercise 3
word = input('Enter Word: ')
letter = input('Enter letter to count: ')
def count(word, letter):
    count = 0
    for Letter in word:
        if Letter == letter:
            count = count + 1
    print(count)
count(word, letter)