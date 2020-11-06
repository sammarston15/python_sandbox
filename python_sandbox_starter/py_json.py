# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample json
userJSON = '{"first_name": "john", "last_name": "doe", "age": 30}'

# parse from json to dict
user = json.loads(userJSON)

# print(user)
# print(user['first_name'])


# parse from dict to json
car = {'make': 'ford', 'model': 'mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)