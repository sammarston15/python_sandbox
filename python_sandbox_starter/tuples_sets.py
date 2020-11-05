# A Tuple is a collection which is ordered and UNCHANGEABLE. Allows duplicate members.
 
# create tuple
fruits = ('apples', 'oranges', 'grapes')
# fruits2 = tuple(('apples', 'oranges', 'grapes')) 

fruits2 = ('apples',) # if there is only one value, ALWAYS leave a trailing comma - this tells python that the data type is a 'tuple' and not a 'string'

# get a value
print(fruits[1])

# =====cannot change value when using tuples (the below code won't work)
# fruits[0] = 'pears'

# delete tuple
del fruits2

# get length
print(len(fruits))






# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {'apples', 'oranges', 'mangos'}

# check if something is in a set
print('apples' in fruits_set) # returns boolean

# add to set
fruits_set.add('grapes')

# remove from set
fruits_set.remove('grapes')

# add duplicate to set
fruits_set.add('apples') # this won't give an error but it just won't add it twice since it is a duplicate

# clear entire set
fruits_set.clear() # this clears it - meaning that the set still exists, it is just empty

# delete entire set
del fruits_set

print(fruits_set)