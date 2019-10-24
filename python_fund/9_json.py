import lib

# Begin
lib.begin()

# Javascript Open Notation
# Is a lightweight data-interchange format. It is easy for humans to read and write. 
# It is easy for humans to read and write.
# It is easy for machines to parse and generate

# It is used primarily to transmit data between a SERVER and a WEB APPLICATION, as an alternative to XML.

# JSON is commonly used with Data APIs. 
# Here is how we can parse JSON into a dic.

import json


'''
JSON
'''
msg = '9. JSON'
lib.print_msg(msg)

user_JSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'


# Parse into a dic
user = json.loads(user_JSON)
print(user_JSON)
print(user)
print(user['first_name'])



print()
# Parse into JSON

car = {'make':'Ford', 'model':'Mustang', 'year':1970}

carJSON = json.dumps(car)
print(car)
print(carJSON)




# End
msg = 'End'
lib.print_end(msg)
