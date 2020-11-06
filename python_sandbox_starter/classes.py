# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create a class
class User:
  # contructor
  def __init__(self, name, email, age): # 'self' is similar to 'this' in JS
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1


# extend class
class Customer(User): # similar definition to JS's `class Customer extends User`
  # contructor
  def __init__(self, name, email, age): # 'self' is similar to 'this' in JS
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# init user object
brad = User('Brad Traversy', 'brad@email.com', 37)
# init customer object
janet = Customer('janet johnson', 'janet@email.com', 25)
janet.set_balance(500)

brad.has_birthday()

print(brad.greeting())
print(janet.greeting())