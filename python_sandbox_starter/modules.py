# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# CORE MODULES
# import datetime
from datetime import date
# import time
from time import time

# PIP MODULES
from camelcase import CamelCase

# import custom module
from validator import validate_email


# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world')) # returns the string with the first letter of each word capitalized


email = 'test@test.com'
if validate_email(email):
  print('email is valid')
else:
  print('email is bad')


# print(timestamp)

# ========== Python's package manger is `pip` ==========
# example: pip3 install camelcase => this will get installed globally