import lib

# Begin
lib.begin()



'''
Classes
'''
msg = '7. Classes'
lib.print_msg(msg)


# A class is a Blueprint for creating objects.
# Objects has properties and methods. 
# Almost everything is an object in Python.
# Python uses self instead of this

class User:

	# Constructor
	def __init__(self, name, email, age):

		self.name = name
		self.email = email
		self.age = age

	def greeting(self):
		return f'My name is {self.name} and I am {self.age}'

	def has_birthday(self):
		self.age += 1


# Inheritance
class Customer(User):

	# Constructor
	def __init__(self, name, email, age):

		self.name = name
		self.email = email
		self.age = age
		self.balance = 0

	# New method
	def set_balance(self, balance):
		self.balance = balance

	# Override existing method
	def greeting(self):
		return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'



# Init user object
brad = User('Brad Traversy', 'btre@gmail', 37)
print(brad)
print(brad.name)
print(brad.age)

brad.age = 38
print(brad.age)
print(brad.greeting())


print()
janet = User('Janet Williams', 'janet@gmail', 27)
janet.has_birthday()
print(janet)
print(janet.name)
print(janet.greeting())



print()

# Init Customer
john = Customer('john Doe', 'john@gmail.com', 40)

john.set_balance(555)
print(john.greeting())


# End
msg = 'End'
lib.print_end(msg)
