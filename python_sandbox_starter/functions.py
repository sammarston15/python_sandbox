# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# create a function
def sayHello(name = 'sam'): # you can set default values in case there is nothing passed into the function (if things are passed in, this is not required)
  print(f'Hello, {name}')

sayHello()

# return values
def getSum(num1, num2):
  total = num1 + num2
  return total

num = getSum(3, 4)

# print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2 # the colon is similar to the arrow in JS and then it will return
print(getSum(10, 3))