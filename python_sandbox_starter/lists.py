# A List is a collection which is ordered and changeable. Allows duplicate members.

# create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# get the value
print(fruits[1])

# get the length
print(len(fruits))

# append to list ( add to the end of the list )
fruits.append('mangos')

# remove from list
fruits.remove('grapes')

# insert into a certain position
fruits.insert(2, 'strawberries') # first param is the position you want to insert at, and the second param is what you are wanting to insert

# remove from a certain position
fruits.pop(2) # remove the item in this position

# change a value
fruits[0] = 'blueberries'

# reverse the list
fruits.reverse()

# sort list
fruits.sort() # sorts alphabetically

# reverse sort
fruits.sort(reverse=True) # sorts reverse alphabetically



print(fruits)