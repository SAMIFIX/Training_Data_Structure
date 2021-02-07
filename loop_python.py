# loop in python


# create list and start add new items
fruits = ['Apple', 'Orange', 'Banana']



# add new items
fruits.append('Tomato')
print('all fruits: ',fruits)

# for loop
for i in fruits:
    print(i + ' #' + str(fruits.index(i)))

# size of list fruits
print('size of fruits list: ',len(fruits))


# range function
for i in range(len(fruits)):
    print(fruits[i])

# slicing fruit list
print('slicing fruits list: ',fruits[::2])


for i in range(1, len(fruits), 3):
    print('range function: ',fruits[i])