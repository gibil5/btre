import lib

# Begin
lib.begin()



'''
Modules
'''
msg = '6. Modules'
lib.print_msg(msg)

# A module is a file containing a set of functions to include in your application. 
# There are:
#	- Core python modules,
# 	- Module you can install using the pip manager, like Django, 
# 	- And custom modules. That you write yourself.



# Core
import datetime
today = datetime.date.today()
print(today)

from datetime import date
today = date.today()
print(today)

print()

import time 
timestamp = time.time()
print(timestamp)

from time import time 
timestamp = time()
print(timestamp)



# Pip
# pip install camelcase
# pip freeze

print()

import camelcase

camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))




import validate

email = 'test@test.com'
if validate.validate_email(email):
	print('Email is valid')
else:
	print('EMail is NOT valid')


email = 'test#test.com'
if validate.validate_email(email):
	print('Email is valid')
else:
	print('EMail is NOT valid')



# End
msg = 'End'
lib.print_end(msg)
