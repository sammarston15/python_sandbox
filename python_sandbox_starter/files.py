# Python has functions for creating, reading, updating, and deleting files.

# create a file
myFile = open('myfile.txt', 'w') # first param is the name of the file, and the second param is the mode (i.e. 'w' for 'write' it to my computer)

# get some info
print('name: ', myFile.name)
print('is closed: ', myFile.closed)
print('opening mode: ', myFile.mode)

# write to file
myFile.write('i love python')
myFile.write(' and javascript')
myFile.close()

# append to a file
myFile = open('myFile.txt', 'a')
myFile.write(' I also like php')
myFile.close()

# read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100) # 100 characters
print(text)

