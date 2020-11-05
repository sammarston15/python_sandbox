# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Sam'
age = 23

# Concatenate
# print('hello, my name is ' + name + ' and I am ' + str(age))

# ==========String Formatting==========
# arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (v3.6+)
# print(f'Hello, my name is {name} and I am {age}') # this is kind of like using backticks in JavaScript, but instead of backticks, it is quotes with the letter 'f' in front of the string.

# ==========String Methods==========
s = 'hello world'

# capitalize string
print(s.capitalize())

# make all uppercase
print(s.upper())

# make all lowercase
print(s.lower())

# swap cases
print(s.swapcase()) # returns opposite case it is currently in (i.e. if all letters are lowercase, it will return the string in all uppercase)

# get length
print(len(s))

# replace
print(s.replace('world', 'everyone')) # replace the word `world` with `everyone` 

# count
sub = 'h'
print(s.count(sub))

# starts with
print(s.startswith('hello')) # returns boolean

# ends with
print(s.endswith('d')) # returns boolean

# split into a list
print(s.split())

# find position
print(s.find('r')) # looks for the first 'r' in the string and give you the position number

# is all alphanumeric
print(s.isalnum()) # returns boolean

# is all alphabetic
print(s.isalpha()) # returns boolean

# is all numberic
print(s.isnumeric()) # returns boolean

