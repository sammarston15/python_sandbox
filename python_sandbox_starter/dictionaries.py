# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# similar to JSON objects or Javascript objects

# create dictionary
person = {
  'first_name': 'john',
  'last_name': 'doe',
  'age': 34
}
print(person, type(person))

# use constructor (optional)
# person2 = dict(first_name='sara', last_name='williams')
# print(person2, type(person2))

# get value
print(person['first_name']) # works like Javascript dot notation
print(person.get('last_name'))

# add key/value
person['phone'] = '111-111-1111'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'boston'

print(person2)

# remove item
del(person['age'])
person.pop('phone')

print(person)

# clear
person.clear()

# get length
print(len(person2))

# list of dict
people = [
  {'name': 'martha', 'age': 30},
  {'name': 'kevin', 'age': 25}
]

print(people[1]['name']) # returns the name of the 2nd item in the list